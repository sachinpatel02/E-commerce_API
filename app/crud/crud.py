from sqlmodel import Session, select, update
from pydantic import EmailStr

from app.core.security import get_password_hash
from app.models.user_model import UserRegister, UserUpdate
from app.schemas.user_schema import User

# fetch user by email id
async def get_user_by_email(session: Session, email: EmailStr):
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

#create_user using UserIn
async def create_user(session: Session, user_in: UserRegister):
    user_data = user_in.model_dump(exclude={"password"})
    hashed_password = get_password_hash(user_in.password)

    new_user = User(**user_data, hashed_password=hashed_password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

# update user
async def update_user(session: Session, user_in: UserUpdate, email: EmailStr):
    statement = update(User).where(User.email == email).values(
        **user_in.model_dump(exclude={"password"})
    )
    session.exec(statement)
    session.commit()
    session.refresh(user)
    return user