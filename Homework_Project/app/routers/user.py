from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models import User, Task
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete

from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get('/user_id')
async def user_by_id(
        db: Annotated[Session, Depends(get_db)],
        user_id: int
):
    user = db.scalar(select(User).where(user_id == User.id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    return user

@router.get('/user_id/tasks')
async def task_by_user_id(
        db: Annotated[Session, Depends(get_db)],
        user_id: int
):
    user = db.scalar(select(User).where(user_id == User.id))
    task = db.scalar(select(Task).where(user_id == Task.user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    return task

@router.post('/create')
async def create_user(
        db: Annotated[Session, Depends(get_db)],
        create_user_model: CreateUser
):
    db.execute(insert(User).values(
        username=create_user_model.username,
        firstname=create_user_model.firstname,
        lastname=create_user_model.lastname,
        age=create_user_model.age,
        slug=slugify(create_user_model.username)
    ))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put('/update')
async def update_user(
        db: Annotated[Session, Depends(get_db)],
        user_id: int,
        update_user_model: UpdateUser
):
    user = db.scalar(select(User).where(user_id == User.id))
    if user is not None:
        db.execute(update(User).where(user_id == User.id).values(
            firstname=update_user_model.firstname,
            lastname=update_user_model.lastname,
            age=update_user_model.age,
        ))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'User update is successful!'
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)],
                      user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        db.execute(delete(User).where(user_id == User.id))
        db.execute(delete(Task).where(user_id == Task.user_id))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'User has been deleted'
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
