from services.users import UserCRUD
from connect_db import get_db


def get_user_crud() -> UserCRUD:
    return UserCRUD(get_db())
