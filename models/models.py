"""
This module defines the User model for the application.
"""

from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    LargeBinary,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from config.database import Session

Base = declarative_base()

class Basemodel:
    """Basemodel for other database tables to inherit"""

    id = Column(String(60), index=True, primary_key=True, default=lambda: str(uuid4()))  # object's unique id
    created_at = Column(DateTime, default=datetime.now(timezone.utc))  # object's creation date
    updated_at = Column(DateTime, default=datetime.now(timezone.utc))  # object's update date

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
    
    def save(self, session: Session): # type: ignore
        """Save object to database"""
        self.updated_at = datetime.now(timezone.utc)
        session.add(self)
        session.commit()
    
    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "__class__" in new_dict:
            del new_dict["__class__"] 
        return new_dict


class Project(Basemodel, Base):
    __tablename__ = 'projects'

    title = Column(String(30), index=True, nullable=False)

    # One-to-Many relationship with Image
    images = relationship("Image", back_populates="project", cascade="all, delete-orphan")



class Image(Basemodel, Base):
    __tablename__ = "images"
    
    image_data = Column(LargeBinary, nullable=True)  # Optional BLOB storage for the image
    image_url = Column(String(255), nullable=False)  # URL of the original image
    annotated_image_url = Column(String(255), nullable=True)  # URL of the annotated image
    
    # Foreign key to link to Project
    project_id = Column(String(60), ForeignKey("projects.id"), nullable=False)
    
    # Relationship back to Project
    project = relationship("Project", back_populates="images")