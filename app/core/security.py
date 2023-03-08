from passlib.context import CryptContext
from jose import jwt
import datetime
import system_config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return pwd_context.verify_password(password, hash)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)})
    return jwt.encode(to_encode, system_config.secret_key, algorithm=system_config.algorithm)


def decode_access_token(token: dict) -> str:
    try:
        encoded_jwt = jwt.decode(token, system_config.secret_key, algorithms=[system_config.secret_key])
    except jwt.JWSError:
        return None
    return encoded_jwt
