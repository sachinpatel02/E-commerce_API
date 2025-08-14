from fastapi import APIRouter, status, Depends, HTTPException
from pydantic import EmailStr
from sqlmodel import Session

from app.core.auth import user_validation_token, verify_current_user
from app.crud.crud import get_user_by_email, update_user
from app.db.session import create_session
from app.models.user_model import UserProfile, UserUpdate

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/me", response_model=UserProfile, status_code=status.HTTP_200_OK)
async def get_profile(username: EmailStr = Depends(user_validation_token), session: Session = Depends(create_session)):
    user = await get_user_by_email(email=username, session=session)
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return user


@user_router.put("/me", response_model=UserUpdate, status_code=status.HTTP_200_OK)
async def update_profile(user_data: UserUpdate, username: EmailStr = Depends(user_validation_token),session: Session = Depends(create_session)):
    user = await get_user_by_email(email=username, session=session)
    updated_user = await update_user(session, user_data, username)
    return updated_user
