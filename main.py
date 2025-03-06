from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, validator
from typing import Optional

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None

    @validator('age')
    def age_must_be_positive(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Age must be a positive integer')
        return v

    is_subscribed: Optional[bool] = False

# Список для хранения пользовательских данных (в реальном приложении используйте базу данных)
users = []

@app.post("/create_user")
async def create_user(user: UserCreate):
    # Добавляем пользователя в список
    users.append(user)
    
    # Возвращаем ответ с полученной информацией
    return {
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "is_subscribed": user.is_subscribed
    }
