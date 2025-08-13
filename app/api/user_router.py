from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session

from app.crud.crud import get_user_by_email, create_user
from app.db.session import create_session
from app.models.user_model import User, UserIn

user_router = APIRouter(prefix="/users", tags=["users"])


# User Creation
@user_router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserIn, session: Session = Depends(create_session)):
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
    first_name = user_in.first_name
    last_name = user_in.last_name
    password = user_in.password
    mobile_number = user_in.mobile_number
    try:
        if not email or not password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="🚨Email and password are required.",
            )

        user = await get_user_by_email(session, email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="🚨Email already registered.",
            )
        new_user = await create_user(session, user_in)
        print("✅New User created")
        return new_user

    except HTTPException as e:
        raise
    except Exception as error:
        print("⁉️Server Error: Cannot create new user", error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong...",
        )
