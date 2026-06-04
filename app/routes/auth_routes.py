from fastapi import APIRouter
from fastapi import Header

from app.schemas.auth_schema import (
    UserRegister,
    UserLogin
)

from app.services.auth_service import (
    register_user,
    login_user,
    verify_token
)

router = APIRouter()
router = APIRouter(prefix="/api/auth")

@router.post("/register")
def register(
        user: UserRegister
):

    return register_user(user)


@router.post("/login")
def login(
        user: UserLogin
):

    return login_user(user)


@router.get("/verify")
def verify(
        authorization: str = Header(None)
):

    if not authorization:

        return {
            "valid": False
        }

    token = authorization.replace(
        "Bearer ",
        ""
    )

    return verify_token(token)