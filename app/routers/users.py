from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.schemas import UserSchema, SignIn, SignUp, Token
from services.users import UserCRUD
from .depends import get_user_crud, get_current_user
from core.security import create_access_token
from fastapi.security import HTTPBearer
from utils.utils import VerifyToken

router = APIRouter()
token_auth_schema = HTTPBearer()


@router.get('/', response_model=List[UserSchema])
async def get_users(users: UserCRUD = Depends(get_user_crud), limit: int = 100, skip: int = 0):
    return await users.get_users(limit=limit, skip=skip)


@router.post('/', response_model=UserSchema)
async def create(user: SignUp, users: UserCRUD = Depends(get_user_crud)):
    return await users.create_user(u=user)


@router.put('/', response_model=UserSchema)
async def update(id: int, user: SignUp, users: UserCRUD = Depends(get_user_crud)):
    return await users.update_user(id=id, u=user)


@router.get('/{id}', response_model=UserSchema)
async def get_user(id: int, users: UserCRUD = Depends(get_user_crud)):
    return await users.get_user(id=id)


@router.delete('/')
async def delete(id: int, users: UserCRUD = Depends(get_user_crud)):
    await users.delete_user(id=id)
    return {"message": "Item deleted successfully"}


@router.post('/login', response_model=Token)
async def login(login: SignIn, users: UserCRUD = Depends(get_user_crud)):
    user = await users.get_by_email(login.email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='incorrect username or password')
    return Token(
        access_token=create_access_token({"sub": user.email}),
        token_type="Bearer"
    )


@router.get('/me')
async def get_me(email: str, users: UserCRUD = Depends(get_user_crud), token: str = Depends(token_auth_schema)):
    if token is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return await users.get_by_email(email=email)
