from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.auth_service import AuthService
from db.repository import UserRepository
from domain.models.user import UserCreate
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

# Dependency that provides AuthService with a UserRepository
def get_auth_service(db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    return AuthService(user_repository)

@router.post("/register")
def register(user: UserCreate, auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.register(user)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.login(form_data.username, form_data.password)
