from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, HttpUrl, ConfigDict
from typing import List, Optional


class ImageSchema(BaseModel):
    id: UUID # Image unique identifier
    image_url: HttpUrl  # URL of the original image
    annotated_image_url: Optional[HttpUrl] = None  # URL of the annotated image
    project_id: UUID  # The UUID of the associated project
    created_at: datetime  # Creation timestamp
    updated_at: datetime  # Last updated timestamp

    model_config = ConfigDict(from_attributes=True)


class ProjectSchema(BaseModel):
    id: UUID  # Project unique identifier
    title: str  # Project title
    images: List[ImageSchema] = []  # List of associated images
    created_at: datetime  # Creation timestamp
    updated_at: datetime  # Last updated timestamp

    model_config = ConfigDict(from_attributes=True)


class CreateImageSchema(BaseModel):
    image_url: HttpUrl  # URL of the original image
    annotated_image_url: Optional[HttpUrl] = None  # URL of the annotated image
    project_id: UUID  # The UUID of the associated project


class CreateProjectSchema(BaseModel):
    title: str  # Project title
