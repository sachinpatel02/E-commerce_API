"""
user_router.py:
    1. get user details
    2. update user details
"""

from fastapi import APIRouter, status, Depends, HTTPException
from pydantic import EmailStr
from sqlmodel import Session

from app.core.auth import user_validation_token
from app.crud.crud import get_user_by_email, update_user
from app.db.session import create_session
from app.models.user_model import UserProfile, UserUpdate

user_router = APIRouter(prefix="/users", tags=["users"])


# get profile
@user_router.get("/me", response_model=UserProfile, status_code=status.HTTP_200_OK)
async def get_profile(username: EmailStr = Depends(user_validation_token), session: Session = Depends(create_session)):
    """
    Get user Profile
    **:input:**
        - login - token
    **:output:**
        - email
        - first_name
        - last_name
        - mobile_number
    """
    user = await get_user_by_email(email=username, session=session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="🚨User not found"
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="🚨User not active"
        )
    return user


# update profile
@user_router.put("/me", response_model=UserUpdate, status_code=status.HTTP_200_OK)
async def update_profile(user_data: UserUpdate, username: EmailStr = Depends(user_validation_token),
                         session: Session = Depends(create_session)):
    """
    Update User Profile
    **:input:**
        - login - token
        - email (Optional)
        - first_name (Optional)
        - last_name (Optional)
        - mobile_number (Optional)

    **:output:**
        - updated email
        - updated first_name
        - updated last_name
        - updated mobile_number
    """
    user = await get_user_by_email(email=username, session=session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="🚨User not found"
        )
    updated_user = await update_user(session, user, user_data)
    return updated_user


# get user by email - 🛑Admin Access required
@user_router.get("/find/", response_model=UserProfile, status_code=status.HTTP_200_OK)
async def get_all_users(q: EmailStr, session: Session = Depends(create_session),
                        username: EmailStr = Depends(user_validation_token)):
    user = await get_user_by_email(email=username, session=session)
    # check for admin access
    if not user or not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="⚠️Admin access required!"
        )
    # get all users
    find_user = await get_user_by_email(email=q, session=session)
    return find_user
