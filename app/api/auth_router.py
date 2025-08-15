"""
auth_router.py:
    1. Register new user
    2. Login

"""

from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.core.auth import generate_token
from app.core.security import verify_password
from app.crud.crud import get_user_by_email, create_user
from app.db.session import create_session
from app.models.user_model import User, UserRegister

auth_router = APIRouter(prefix="/auth", tags=["users", "auth"])


# User Creation
@auth_router.post(
    "/", response_model=User,
    status_code=status.HTTP_201_CREATED,
    description="Create a new user",
    response_description="✅New User created"
)
async def register(user_in: UserRegister, session: Session = Depends(create_session)):
    """
    # Register a new user
    **:input:**
        - email: EmailStr
        - password:
        - first_name: String
        - last_name: String
        - mobile_number: String - Optional

    **:output:**
        email: EmailStr
        name: String (first_name + last_name)
    """
    email = user_in.email
    password = user_in.password
    try:
        # 1. check if we have email and password
        if not email or not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="🚨Email and password are required.",
            )

        # 2. check if the user already exist
        user = await get_user_by_email(session, email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="🚨Email already registered.",
            )
        # 3. create new user
        new_user = await create_user(session, user_in)
        print("✅New User created")
        return new_user

    except HTTPException as e:
        raise e
    except Exception as error:
        print("⁉️Server Error: Registration Failed!", error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong...",
        )


# User Login
@auth_router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    description="Login Route",
    response_description="❇️Successfully logged in",
)
async def login(session: Session = Depends(create_session), user_in: OAuth2PasswordRequestForm = Depends()):
    """
    # Login Route
    **:input:**
        - email: EmailStr
        - password:
    **:output:**
        - email: EmailStr
        - first_name
        - last_name
        - mobile_number
    """
    try:
        email = user_in.username
        password = user_in.password

        if not email or not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="🚨Email and password are required.",
            )

        user = await get_user_by_email(session, email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="🚨User not found."
            )
        if not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="🚨Invalid Username or Password."
            )
        login_token = generate_token(data={"sub": user.email})
        return {"login_token": login_token, "token_type": "bearer"}
    except HTTPException as e:
        raise e
    except Exception as error:
        print("⁉️Server Error: Login Failed!", error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong...",
        )
