import streamlit as st
import requests
from uuid import UUID

# FastAPI backend URL
backend_url = "https://label-box-backend.onrender.com"

# Function to create a new project
def create_project(title):
    response = requests.post(f"{backend_url}/projects", json={"title": title})
    if response.status_code == 201:
        st.success("Project created successfully!")
    else:
        st.error("Failed to create project")

# Function to get a project by ID
def get_project(project_id):
    response = requests.get(f"{backend_url}/projects/{project_id}")
    if response.status_code == 200:
        project = response.json()
        st.write("Project Title:", project["title"])
    else:
        st.error("Project not found")

# Streamlit app layout
st.title("Project Management")

# Create project section
st.header("Create a New Project")
project_title = st.text_input("Project Title")
if st.button("Create Project"):
    create_project(project_title)

# Get project section
st.header("Get Project Details")
project_id = st.text_input("Project ID")
if st.button("Get Project"):
    get_project(project_id)