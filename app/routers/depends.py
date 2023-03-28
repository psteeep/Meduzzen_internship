from services.users import UserCRUD
from connect_db import get_db
from schemas.schemas import UserSchema
from fastapi import Depends, HTTPException, status
from core.security import decode_access_token
from fastapi.security import HTTPBearer

token_auth_schema = HTTPBearer()
db = get_db()


def get_user_crud() -> UserCRUD:
    return UserCRUD(get_db())


async def get_current_user(
        # users: UserCRUD = Depends(get_user_crud),
        db=db,
        token: str = Depends(token_auth_schema),
):
    users = UserCRUD(db)
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Credentials are not valid")
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception
    email: str = payload.get("sub")
    if email is None:
        raise cred_exception
    user = await users.get_by_email(email=email)
    if user is None:
        return cred_exception
    return user
