from typing import Union
from utils import sample

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",  # Add the URLs of your frontend applications
    "http://localhost:3000",  # If your frontend is running on a different port
    "https://yourfrontenddomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # You can specify specific headers if needed
)
@app.get("/")
def read_root():
    return sample.outputFun()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
