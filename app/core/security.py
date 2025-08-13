from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from .config import configs

# loading secrets from dotenv
SECRET_KEY = configs.SECRET_KEY
ALGORITHM = configs.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = configs.ACCESS_TOKEN_EXPIRE_MINUTES

# using bcrypt for cryptography
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# encrypt password
def get_password_hash(password: str) -> str:
    return password_context.hash(password)


# decrypt password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


# create access token
def generate_token(data: dict):
    # setting expiry time
    expires = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # adding it to the data
    data.update({"exp": expires})
    # generating token using data, secret_key and algorithm
    encoded_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_token
