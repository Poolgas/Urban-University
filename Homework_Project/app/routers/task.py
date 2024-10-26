from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from app.models import Task, User
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    if tasks is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Table is empty')
    return tasks


@router.get('/task_id')
async def task_by_id(
        db: Annotated[Session, Depends(get_db)],
        task_id: int
):
    task = db.scalar(select(Task).where(task_id == Task.id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')
    return task


@router.post('/create')
async def create_task(
        db: Annotated[Session, Depends(get_db)],
        create_task_model: CreateTask,
        user_id: int
):
    user = db.scalar(select(User).where(user_id == User.id))
    if user is not None:
        db.execute(insert(Task).values(
            title=create_task_model.title,
            content=create_task_model.content,
            priority=create_task_model.priority,
            user_id=user_id,
            slug=slugify(create_task_model.title)
        ))
        db.commit()
        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')


@router.put('/update')
async def update_task(
        db: Annotated[Session, Depends(get_db)],
        task_id: int,
        update_task_model: UpdateTask
):
    task = db.scalar(select(Task).where(task_id == Task.id))
    if task is not None:
        db.execute(update(Task).where(task_id == Task.id).values(
            title=update_task_model.title,
            content=update_task_model.content,
            priority=update_task_model.priority,
        ))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Task update is successful!'
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)],
                      task_id: int):
    task = db.scalar(select(Task).where(task_id == Task.id))
    if task is not None:
        db.execute(delete(Task).where(task_id == Task.id))
        db.commit()
        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Task has been deleted'
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found')
