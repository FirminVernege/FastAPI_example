from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, vote

"""
unwanted imports
from .config import settings
from .database import engine
from pydantic_settings import BaseSettings
from . import models
"""


#Create instance of FastApi
app = FastAPI()

origins = ["*"] #Set to everyone. needs configuration 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#models.Base.metadata.create_all(bind=engine)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Welcome to my api, bro"}



