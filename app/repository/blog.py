from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, Response, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(db: Session, request: schemas.Blog):
    new_blog = models.Blog(title=request.title,
                           body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")

    blog.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


def update(db: Session, id: int, request: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")

    blog.update(vars(request))
    db.commit()
    return "updated"


def get_id(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")

    return blog
