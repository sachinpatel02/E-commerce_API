from fastapi import APIRouter, HTTPException, Depends, status

from app.core.auth import verify_current_user
from app.models.user_model import UserProfile

user_router = APIRouter(prefix="/users", tags=["user"])


@user_router.get("/me", response_model=UserProfile)
async def get_profile(profile: UserProfile = Depends(verify_current_user)):
    if not profile.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return profile
