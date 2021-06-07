from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, schemas
from app.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(db, request)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return user.get_id(db, id)
