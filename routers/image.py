import os
from fastapi import APIRouter, UploadFile, Form, HTTPException, Depends
from sqlalchemy.orm import Session
import cloudinary
import cloudinary.uploader
from uuid import UUID

from config.database import get_session
from models.models import Image, Project
from models.schemas import ImageSchema

# Initialize Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

router = APIRouter()

@router.post("/projects/{project_id}/upload-image", response_model=ImageSchema, status_code=201)
def upload_image(
    project_id: UUID,
    file: UploadFile,
    db: Session = Depends(get_session)
):
    """
    Upload an image to Cloudinary, create an Image object, and tie it to a project.
    """
    # Validate if the project exists
    project = db.query(Project).filter(Project.id == str(project_id)).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Upload the file to Cloudinary
    try:
        cloudinary_response = cloudinary.uploader.upload(
            file.file, 
            folder=f"projects/{project_id}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading to Cloudinary: {e}")
    
    # Extract the Cloudinary URL
    image_url = cloudinary_response.get("secure_url")
    if not image_url:
        raise HTTPException(status_code=500, detail="Failed to retrieve Cloudinary URL")

    # Create the Image object and tie it to the project
    image = Image(
        project_id=str(project_id),
        image_url=image_url,
        annotated_image_url=None
    )
    db.add(image)
    db.commit()
    db.refresh(image)

    # Return the Image object schema
    return ImageSchema.model_validate(image)