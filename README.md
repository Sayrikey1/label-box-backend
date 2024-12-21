# Label Box 🏷️

A simple label box application using FastAPI and Streamlit. This application uses Cloudinary for media storage and PostgreSQL as a database. It performs all the necessary CRUD operations required for a label box application.

## 🚀 Deployments

- 🔗 **Backend URL**: [Label Box Backend](https://label-box-backend.onrender.com)
- 🔗 **Frontend URL**: [Label Box Frontend](https://label-box-backend-htld236vutbbhx9t5fleyu.streamlit.app)

## 📦 Project Repository

- 👤 **GitHub Profile**: [Sayrikey1](https://github.com/Sayrikey1)
- 📦 **Project Repo**: [Label Box Backend](https://github.com/Sayrikey1/label-box-backend)

## 🛠️ Installation and Setup

### Prerequisites

- Python 3.10+
- PostgreSQL
- Cloudinary account

### Clone the Repository

```sh
git clone https://github.com/Sayrikey1/label-box-backend.git
cd label-box-backend
```

### Create and Activate a Virtual Environment

To set up an isolated Python environment for the project:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

Install all the required Python packages from the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```env
DB_NAME=your_db_name
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_USERNAME=your_db_username
CLOUDINARY_NAME=your_cloudinary_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
```

### Run Database Migrations

Apply the database migrations using Alembic:

```sh
alembic upgrade head
```

### Run the Backend Server

Start the FastAPI backend server:

```sh
uvicorn main:app --reload
```

### Run the Frontend Application

Navigate to the `front` directory and run the Streamlit app:

```sh
cd front
streamlit run app.py
```

## 📚 Usage

### Create a New Project

1. Go to the "Create a New Project" section.
2. Enter the project title.
3. Click the "Create Project" button.

### Get Project Details

1. Go to the "Get Project Details" section.
2. Enter the project ID.
3. Click the "Get Project" button.

### Get All Projects

1. Go to the "Get All Projects" section.
2. Click the "Get All Projects" button.

### Get Image Details

1. Go to the "Get Image Details" section.
2. Enter the image ID.
3. Click the "Get Image" button.

### Upload Image to Project

1. Go to the "Upload Image to Project" section.
2. Enter the project ID for image upload.
3. Choose an image file.
4. Click the "Upload Image" button.

## 🖍️ License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📧 Contact

For any inquiries, please contact [Sayrikey1](https://github.com/Sayrikey1).

---

Made with ❤️ by Sayrikey1