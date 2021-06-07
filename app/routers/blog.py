from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app import schemas, database, oauth2
from app.repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_active_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_active_user)):
    return blog.create(db, request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_active_user)):
    return blog.get_id(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_active_user)):
    return blog.update(db, id, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_active_user)):
    return blog.destroy(db, id)
