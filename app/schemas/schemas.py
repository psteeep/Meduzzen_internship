from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class SignIn(BaseModel):
    email: str
    password: str


class SignUp(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    name: str
    email: str


class UserBaseResponse(BaseModel):
    id: int
    name: str
    email: str
