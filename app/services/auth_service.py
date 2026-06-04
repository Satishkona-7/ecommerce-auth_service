from datetime import datetime
from datetime import timedelta

from jose import jwt
from jose import JWTError

from passlib.context import CryptContext

from app.database import user_collection

from app.config import (
    JWT_SECRET,
    JWT_ALGORITHM,
    TOKEN_EXPIRE_MINUTES
)

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password):

    return pwd_context.hash(password)


def verify_password(
        plain_password,
        hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def register_user(user):

    existing_user = user_collection.find_one(
        {
            "username": user.username
        }
    )

    if existing_user:

        return {
            "success": False,
            "message": "User already exists"
        }

    user_collection.insert_one(
        {
            "username": user.username,
            "password": hash_password(
                user.password
            )
        }
    )

    return {
        "success": True,
        "message": "User registered"
    }


def create_access_token(username):

    expire = datetime.utcnow() + timedelta(
        minutes=TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": username,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )

    return token


def login_user(user):

    db_user = user_collection.find_one(
        {
            "username": user.username
        }
    )

    if not db_user:

        return {
            "success": False,
            "message": "Invalid credentials"
        }

    if not verify_password(
            user.password,
            db_user["password"]
    ):

        return {
            "success": False,
            "message": "Invalid credentials"
        }

    token = create_access_token(
        user.username
    )

    return {
        "success": True,
        "access_token": token
    }


def verify_token(token):

    try:

        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALGORITHM]
        )

        username = payload.get("sub")

        return {
            "valid": True,
            "username": username
        }

    except JWTError:

        return {
            "valid": False
        }