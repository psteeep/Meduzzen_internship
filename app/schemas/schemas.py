from pydantic import BaseModel, validator, Field
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    password: Optional[str]


class SignIn(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class SignUp(BaseModel):
    name: str
    email: str
    password: str = Field(min_length=8, max_length=32)
    password2: str = Field(min_length=8, max_length=32)

    @validator('password2')
    def passwords_match(cls, password2, values):
        if 'password' in values and password2 != values['password']:
            raise ValueError('passwords don`t match')
        return password2

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: str
    email: str


class UserBaseResponse(BaseModel):
    id: int
    name: str
    email: str
