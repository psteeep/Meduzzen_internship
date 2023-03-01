from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class SignIn(BaseModel):
    email: str
    password: str
    status: str


class SignUp(BaseModel):
    email: str
    password: str
    status: str


class UserUpdate(BaseModel):
    name: str
    status: str


class UserBaseResponse(BaseModel):
    id: int
    name: str
    email: str
