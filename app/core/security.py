from passlib.context import CryptContext

# using bcrypt for cryptography
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# encrypt password
def get_password_hash(password: str) -> str:
    return password_context.hash(password)


# decrypt password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)
