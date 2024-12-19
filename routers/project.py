from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import UUID4
from typing import List
from config.database import get_session  # Assume you have a `get_session` dependency for the database session
from models.models import Project, Image  # Assume `Project` and `Image` models are defined as in your schema
from models.schemas import ProjectSchema, CreateProjectSchema, ImageSchema  # Use the schemas we defined earlier

router = APIRouter()

# Create a new project
# Create a new project
@router.post("/projects", status_code=201, response_model=ProjectSchema)
def create_project(project: CreateProjectSchema, db: Session = Depends(get_session)):
    """Create a new project."""
    new_project = Project(
        title=project.title,
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return ProjectSchema.model_validate(new_project)


# Get a project along with the IDs of its related images
@router.get("/projects/{project_id}", status_code=200, response_model=ProjectSchema)
def get_project(project_id: UUID, db: Session = Depends(get_session)):
    """Retrieve a project and its associated image IDs."""
    project = db.query(Project).filter(Project.id == str(project_id)).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return ProjectSchema.model_validate(project)

@router.get("/projects", status_code=200, response_model=List[ProjectSchema])
def get_all_projects(db: Session = Depends(get_session)):
    """Retrieve all projects and their associated image IDs."""
    projects = db.query(Project).all()
    return [ProjectSchema.model_validate(project) for project in projects]

