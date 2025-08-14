from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from pydantic import EmailStr
from sqlmodel import Session

from app.core.config import configs
from app.crud.crud import get_user_by_email
from app.db.session import create_session

# loading secrets from dotenv
SECRET_KEY = configs.SECRET_KEY
ALGORITHM = configs.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = configs.ACCESS_TOKEN_EXPIRE_MINUTES


# create access token
def generate_token(data: dict):
    # setting expiry time
    expires = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # adding it to the data
    data.update({"exp": expires})
    # generating token using data, secret_key and algorithm
    encoded_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_token


# get current user
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def verify_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: Session = Depends(create_session)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: EmailStr = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="🚨Token is missing required claims.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        user = get_user_by_email(session, username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="🚨User not found.",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="🚨Invalid or expired token.",
            headers={"WWW-Authenticate": "Bearer"},
        )


# user validation using token, from SwaggerUI's built-in login functionality
bearer_schema = HTTPBearer()


def user_validation_token(creds: Annotated[HTTPAuthorizationCredentials, Depends(bearer_schema)]):
    token = creds.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found.",
            )
        return username
    except JWTError:
        raise
