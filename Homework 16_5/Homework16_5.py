'''
Домашнее задание по теме "Шаблонизатор Jinja 2."

Цель: научиться взаимодействовать с шаблонами Jinja 2 и использовать их в запросах.

Задача "Список пользователей в шаблоне":
Подготовка:
Используйте код из предыдущей задачи.
Скачайте заготовленные шаблоны для их дополнения.
Шаблоны оставьте в папке templates у себя в проекте.
Создайте объект Jinja2Templates, указав в качестве папки шаблонов - templates.
Измените и дополните ранее описанные CRUD запросы:
Напишите новый запрос по маршруту '/':
Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request и список users. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
Измените get запрос по маршруту '/users' на '/users/{user_id}':
Функция по этому запросу теперь принимает аргумент request и user_id.
Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request и одного из пользователей - user. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
Создайте несколько пользователей при помощи post запроса со следующими данными:
username - UrbanUser, age - 24
username - UrbanTest, age - 22
username - Capybara, age - 60
В шаблоне 'users.html' заготовлены все необходимые теги и обработка условий, вам остаётся только дополнить закомментированные строки вашим Jinja 2 кодом (использование полей id, username и age объектов модели User):
1. По маршруту '/' должен отображаться шаблон 'users.html' со списком все ранее созданных объектов:
2. Здесь каждая из записей является ссылкой на описание объекта, информация о котором отображается по маршруту '/users/{user_id}':
'''
from fastapi import FastAPI, HTTPException, Path, Request, Form
from fastapi.responses import HTMLResponse
from typing import List, Annotated
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/users/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, 'user': users[user_id-1]})


@app.post('/users/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(min_length=3, max_length=30, description='Enter username', example='Kirill')]
        , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=30)]) -> User:
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=0, le=300, description='Enter user_id', example='1')]
        , username: Annotated[str, Path(min_length=3, max_length=30, description='Enter username', example='Kirill')]
        , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=30)]) -> User:
    try:
        user = next((u for u in users if u.id == user_id))
        users[user_id-1] = User(id=user.id, username=username, age=age)
        return users[user_id]
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/users/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=0, le=300, description='Enter user_id', example='1')]) -> User:
    try:
        user = next((u for u in users if u.id == user_id))
        users.remove(user)
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")
