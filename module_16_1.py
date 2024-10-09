from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Главная страница."}


@app.get("/user/admin")
async def Admin():
    return {"message": "Вы вошли как администратор."}


@app.get("/user/{user_id}")
async def id_(user_id):
    return {"message": f"Вы вошли как пользователь № {user_id}."}


@app.get("/user")
async def quest(username, age):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}."}
