from fastapi import APIRouter, HTTPException, Depends
from config.jwt_utils import verify_token

router = APIRouter()

@router.get("/protected_resource/")
def protected_resource(token):
    username = verify_token(token)
    return {"message": f"Hello {username}! Access granted."}