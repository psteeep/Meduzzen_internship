from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.schemas import UserSchema, SignIn, SignUp
from services.users import UserCRUD
from .depends import get_user_crud

router = APIRouter()


@router.get('/', response_model=List[UserSchema])
async def get_users(users: UserCRUD = Depends(get_user_crud), limit: int = 100, skip: int = 100):
    return await users.get_users(limit=limit, skip=skip)


@router.post('/', response_model=UserSchema)
async def create(user: SignUp, users: UserCRUD = Depends(get_user_crud)):
    return await users.create_user(u=user)


@router.put('/', response_model=UserSchema)
async def update(id: int, user: SignUp, users: UserCRUD = Depends(get_user_crud)):
    return await users.update_user(id=id, u=user)


@router.get('/', response_model=UserSchema)
async def get_user(id: int, users: UserCRUD = Depends(get_user_crud)):
    return await users.get_user(id=id)


@router.delete('/', response_model=UserSchema)
async def delete(id: int, users: UserCRUD = Depends(get_user_crud)):
    return {}
