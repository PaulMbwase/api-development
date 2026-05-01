from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional


class PostBase(BaseModel): # For validation purpose
    title: str
    content: str 
    published: bool = True 
    



class PostCreate(PostBase): # For validation purpose
    pass 


class UpdatePost(PostBase): # For validation purpose
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime 
    #password: str

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime 
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode  = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True
#################
#### USERS
################


class UserCreate(BaseModel):
    email: EmailStr
    password: str




class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] | None = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # type: ignore