from fastapi import APIRouter, HTTPException, status, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
import secrets

from db.users import USER_DATA
from config.pass_hashing import verify_password
from config.jwt_utils import create_access_token
from models import UserCreate, TokenResponse

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()

@router.post("/login", response_model=TokenResponse)
@limiter.limit("5/minute")
def login_user(request: Request, data: UserCreate):
    user = next((u for u in USER_DATA if secrets.compare_digest(u.username, data.username)), None)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization failed")

    token = create_access_token(user.username)
    return {"access_token": token, "token_type": "bearer"}
