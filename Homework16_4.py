'''
Домашнее задание по теме "Модели данных Pydantic"
Цель: научиться описывать и использовать Pydantic модель.

Задача "Модель пользователя":
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
id - номер пользователя (int)
username - имя пользователя (str)
age - возраст пользователя (int)

Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
'''
from fastapi import FastAPI, HTTPException, Path
from typing import List, Annotated
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/user')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(
        username: Annotated[str, Path(min_length=3, max_length=30, description='Enter username', example='Kirill')]
        , age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=30)]) -> User:
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
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


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=0, le=300, description='Enter user_id', example='1')]) -> User:
    try:
        user = next((u for u in users if u.id == user_id))
        users.remove(user)
        return user
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")
