from core.security import hash_password, verify_password, create_access_token
from domain.models.user import UserCreate
from domain.interfaces.repository import UserRepositoryInterface
from fastapi import HTTPException, status


class AuthService:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def register(self, user: UserCreate):
        existing_user = self.user_repository.get_user_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed_password = hash_password(user.password)
        return self.user_repository.create_user(user.username, user.email, hashed_password)

    def login(self, username: str, password: str):
        user = self.user_repository.get_user_by_username(username)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        # Generate JWT token using PyJWT
        access_token = create_access_token(data={"sub": user.username})
        return {"access_token": access_token, "token_type": "bearer"}
