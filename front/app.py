import streamlit as st
import requests
from streamlit_img_label import st_img_label

# FastAPI backend URL
backend_url = "https://label-box-backend.onrender.com"
frontend_url = "https://label-box-backend-htld236vutbbhx9t5fleyu.streamlit.app"

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
        with st.container():
            st.subheader(project["title"])
            st.write("Project ID:", project["id"])
            st.write("Created At:", project["created_at"])
            st.write("Updated At:", project["updated_at"])
            st.write("Images:")
            for image in project["images"]:
                st.image(image["image_url"], caption="Original Image", use_container_width=True)
                if image["annotated_image_url"]:
                    st.image(image["annotated_image_url"], caption="Annotated Image", use_container_width=True)
                st.write("Image ID:", image["id"])
    else:
        st.error("Project not found")

# Function to get all projects
def get_all_projects():
    response = requests.get(f"{backend_url}/projects")
    if response.status_code == 200:
        projects = response.json()
        for project in projects:
            with st.container():
                st.subheader(project["title"])
                st.write("Project ID:", project["id"])
                st.write("Created At:", project["created_at"])
                st.write("Updated At:", project["updated_at"])
                st.write("Images:")
                for image in project["images"]:
                    st.image(image["image_url"], caption="Original Image", use_container_width=True)
                    if image["annotated_image_url"]:
                        st.image(image["annotated_image_url"], caption="Annotated Image", use_container_width=True)
                    st.write("Image ID:", image["id"])
                st.write("---")
    else:
        st.error("Failed to retrieve projects")

# Function to get an image by ID
def get_image(image_id):
    response = requests.get(f"{backend_url}/images/{image_id}")
    if response.status_code == 200:
        image = response.json()
        with st.container():
            st.image(image["image_url"], caption="Original Image", use_container_width=True)
            if image["annotated_image_url"]:
                st.image(image["annotated_image_url"], caption="Annotated Image", use_container_width=True)
            st.write("Image ID:", image["id"])
            st.write("Project ID:", image["project_id"])
            st.write("Uploaded At:", image["uploaded_at"])

            # Image labeling
            labels = st_img_label(image["image_url"], key="label_image")
            if st.button("Save Annotations"):
                annotated_image_url = save_annotations(image_id, labels)
                if annotated_image_url:
                    st.success("Annotations saved successfully!")
                    st.image(annotated_image_url, caption="Annotated Image", use_container_width=True)
    else:
        st.error("Image not found")

# Function to save annotations
def save_annotations(image_id, labels):
    response = requests.post(f"{backend_url}/images/{image_id}/annotate", json={"labels": labels})
    if response.status_code == 200:
        return response.json()["annotated_image_url"]
    else:
        st.error("Failed to save annotations")
        return None

# Function to upload an image
def upload_image(project_id, image_file):
    files = {"file": image_file}
    response = requests.post(f"{backend_url}/projects/{project_id}/upload-image", files=files)
    if response.status_code == 201:
        st.success("Image uploaded successfully!")
    else:
        st.error("Failed to upload image")

# Streamlit app layout
st.title("Label Box 🏷️")

st.write("A simple label box application using FastAPI and Streamlit.")

# Project information
st.write(f"🔗 Backend URL: {backend_url}")
st.write(f"🔗 Frontend URL: {frontend_url}")

# Write 
st.write("This application uses Cloudinary for media storage and PostgreSQL as a database. It performs all the necessary CRUD operations required for a label box application.")

# Add a link to your GitHub profile
st.markdown("👤 [GitHub Profile](https://github.com/Sayrikey1)")
st.markdown("📦 [Project Repo](https://github.com/Sayrikey1/label-box-backend)")

# Create project section
st.header("Create a New Project 🆕")
project_title = st.text_input("Project Title")
if st.button("Create Project"):
    create_project(project_title)

# Get project section
st.header("Get Project Details 🔍")
project_id = st.text_input("Project ID")
if st.button("Get Project"):
    get_project(project_id)

# Get all projects section
st.header("Get All Projects 📋")
if st.button("Get All Projects"):
    get_all_projects()

# Get image section
st.header("Get Image Details 🖼️")
image_id = st.text_input("Image ID")
if st.button("Get Image"):
    get_image(image_id)

# Upload image section
st.header("Upload Image to Project 📤")
upload_project_id = st.text_input("Project ID for Image Upload")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if st.button("Upload Image"):
    if uploaded_file is not None:
        upload_image(upload_project_id, uploaded_file)
    else:
        st.error("Please select an image file to upload.")