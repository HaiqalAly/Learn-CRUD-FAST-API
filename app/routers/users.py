from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, cast

from app.database.database import get_db
from app.database.models import User
from app.schemas.user import UserResponse, UserCreate
from app.dependencies import get_current_active_user
from app.core import security
from app.schemas.user import UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return db.query(User).all()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    return user

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, update_user: UserCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found!")

    existing_user.name = cast(str, update_user.name)
    existing_user.email = cast(str, update_user.email)
    existing_user.role = cast(str, update_user.role)

    db.commit()
    db.refresh(existing_user)
    return existing_user

@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    if user.id == current_user.id:
        raise HTTPException(status_code=400, detail="Users cannot delete themselves!")

    db.delete(user)
    db.commit()
    return

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    """
    Creates a new user account. Requires an active user (e.g., Admin) token.
    """
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered!")
    
    hashed_password = security.get_password_hash(user.password)
    new_user = User(
        name=user.name,
        email=user.email,
        role=user.role,
        hashed_pwd=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
