from models import User
from schemas.schemas import UserSchema, UserUpdate, SignUp, SignIn, UserBaseResponse
from typing import List, Optional
from core.security import hash_password
from .base import BaseRepository


class UserCRUD(BaseRepository):

    async def get_users(self, skip: int = 0, limit: int = 100) -> List[UserSchema]:
        query = User.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_user(self, id: int) -> Optional[UserSchema]:
        query = User.select.where(User.c.id == id).first()
        user = await self.database.fetch_one(query)
        if user is None:
            return None
        return UserSchema.parse_obj(User)

    async def create_user(self, u: SignUp) -> UserSchema:
        user = UserSchema(
            name=u.name,
            hashed_password=hash_password(u.password),
            emai=u.email
        )
        values = {**user.dict()}
        values.pop('id', None)
        query = user.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update_user(self, id: int, u: SignUp) -> UserSchema:
        user = UserSchema(
            name=u.name,
            hashed_password=hash_password(u.password2),
            emai=u.email
        )
        values = {**user.dict()}
        values.pop("created_at", None)
        values.pop("id", None)
        query = user.update().where(user.c.id == id).values(**values)
        await self.database.execute(query)
        return user

    async def delete_user(self) -> UserSchema:
        pass
