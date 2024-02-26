from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # Adjust this to match your React app's origin
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "id": 1, 
        "message": "Hello world"
    }

# http://localhost:5000/user


@app.get("/user")
async def user():
    return {
        "id": 1,
        "name": "Sabbir",
        "email": "sabbir@sab.com",
        "password": "sabbir"
    }
