📁 Structure of backend
CALC/

├── backend/

│   ├── __pycache__/          
│   ├── venv/                 
│   ├── Dockerfile       
│   └── main.py         
├── README.md           
└── requirements.txt


🛠️ Requirements

FastAPI
Pydantic
Uvicorn

pip install -r requirements.txt



venv\scripts\activate
uvicorn main:app --reload



🐳 Dockerfile 
The Dockerfile is used to containerize the backend. 

Base Image: Uses python:3.12-slim for decrease height of image 

Working Directory: /app for working directory.

Dependencies: Installs the required Python packages from requirements.txt.

Expose Port: Exposes port 8000 for the FastAPI app.

Run Command: Starts the app using uvicorn.


