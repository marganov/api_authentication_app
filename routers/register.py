from fastapi import APIRouter, HTTPException, status, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from config.pass_hashing import get_password_hash
from db.users import USER_DATA
from models import UserCreate, UserInDB
import secrets

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()

@router.post("/register/", status_code=status.HTTP_201_CREATED)
@limiter.limit("1/minute")
def register_user(request: Request, data: UserCreate):
    for user in USER_DATA:
        if secrets.compare_digest(user.username, data.username):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Already exists"
            )
    hashed_password = get_password_hash(data.password)
    new_user = UserInDB(username=data.username, hashed_password=hashed_password)
    USER_DATA.append(new_user)
    return {"message": "New user created"}