from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=4, max_length=20, description='Enter username'
    , example='UrbanUser')], age: int = Path(ge=18, le=70, description='Enter age', example='18')) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    add_user = f'Имя: {username}, возраст: {age}'
    users[current_index] = add_user
    return f'User {current_index} is registered.'


@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id: int = Path(ge=0), username: str = Path(min_length=4, max_length=20
    , description='Enter username', example='Urban User'), age: int = Path(ge=18
    , le=70, description='Enter age', example='18')) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated.'


@app.put('/user/{user_id}/{username}/{age}')
async def put_user(user_id: int = Path(ge=0), username: str = Path(min_length=4, max_length=20
    , description='Enter username', example='New User'), age: int = Path(ge=18
    , le=70, description='Enter age', example='22')) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated.'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted.'

