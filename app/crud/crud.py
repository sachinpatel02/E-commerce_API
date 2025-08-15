"""
crud.py:
    * do crud operations
        1. get_user_by_email(session, email) : execute select using email and return the user if found, else return None
        2. create_user(session, UserRegister): hash the password and create a user using add
        3. update_user(session, user, userUpdate): find the user by email and update it with new values using update
"""

from pydantic import EmailStr
from sqlmodel import Session, select, update

from app.core.security import get_password_hash
from app.models.user_model import UserRegister, UserUpdate
from app.schemas.user_schema import User


# fetch user by email id
async def get_user_by_email(session: Session, email: EmailStr):
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()


# create_user using UserIn
async def create_user(session: Session, user_in: UserRegister):
    user_data = user_in.model_dump(exclude={"password"})
    hashed_password = get_password_hash(user_in.password)

    new_user = User(**user_data, hashed_password=hashed_password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


# update user
async def update_user(session: Session, user, user_in: UserUpdate):
    values = {k: v for k, v in user_in.model_dump().items() if v is not None}
    statement = update(User).where(User.email == user.email).values(
        **values
    )
    session.exec(statement)
    session.commit()
    session.refresh(user)
    return user
