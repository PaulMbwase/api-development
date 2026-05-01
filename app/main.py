from typing import Optional, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv, find_dotenv # type: ignore
from . import models, schemas, utils, config
from .database import engine
from .routers import post, user, auth, vote


# models.Base.metadata.create_all(bind=engine)

origins = ["*"]
# fetch('http://localhost:8000/').then(res =>res.json()).then(console.log)


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# request Get method , url: "/"


        

my_posts =[
    {"title": "title of post1", "content":"content of post 1", "id": 1},
    {"title": "favorite foods", "content":"I like Pizza", "id": 2}
    ]

def find_post(id:int):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id:int):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
async def root():
    return {"message": "Welcom to my api, Jesus-Christ loves you so much! Do you believe it?"}





# title str, content str, 

######################## 
##### USERS 
