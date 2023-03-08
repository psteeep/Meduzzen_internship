from models import User
from schemas.schemas import UserSchema, UserUpdate, SignUp, SignIn, UserBaseResponse
from typing import List, Optional
from core.security import hash_password
from .base import BaseRepository
from sqlalchemy import insert, select, update, delete


class UserCRUD(BaseRepository):

    async def get_users(self, skip: int = 0, limit: int = 100) -> List[UserSchema]:
        query = select(User).limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_user(self, id: int) -> Optional[UserSchema]:
        query = select(User).where(User.id == id)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return user

    async def create_user(self, u: SignUp) -> UserSchema:
        user = UserSchema(
            name=u.name,
            email=u.email,
            password=hash_password(u.password),
        )
        values = {**user.dict()}
        values.pop('id', None)
        query = insert(User).values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update_user(self, id: int, u: SignUp) -> UserSchema:
        user = UserSchema(
            name=u.name,
            email=u.email,
            password=hash_password(u.password2)
        )
        values = {**user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = update(User).where(User.id == id).values(**values)
        await self.database.execute(query)
        return user

    async def delete_user(self, id: int):
        query = delete(User).where(User.id == id)
        return await self.database.execute(query)

    async def get_by_email(self, email: str) -> UserSchema:
        query = select(User).where(User.email == email)
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return user
