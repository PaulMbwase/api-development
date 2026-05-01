from .. import models, schemas, utils
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter # type: ignore
from sqlalchemy.orm import Session
from .. database import get_db
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # 1. Hash the password
    hashed_password = utils.hash(user.password)
    
    # 2. Convert Pydantic model to a dict
    user_dict = user.model_dump()
    
    # 3. Replace the plain password with the hashed one in the dict
    user_dict["password"] = hashed_password
    
    # 4. Unpack the modified dict into the SQLAlchemy model
    new_user = models.User(**user_dict)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")
    return user 