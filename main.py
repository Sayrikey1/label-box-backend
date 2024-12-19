from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import models
from config.database import engine
from routers import image, project

# Load environment variables
load_dotenv()

# Initialize the FastAPI application
app = FastAPI()

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust the origins to restrict access as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(project.router)
app.include_router(image.router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}
