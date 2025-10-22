from fastapi import APIRouter, HTTPException, Depends
from config.jwt_utils import oauth2_scheme, verify_token

router = APIRouter()

@router.get("/protected_resource/")
def protected_resource(token=Depends(oauth2_scheme)):
    username = verify_token(token)
    return {"message": f"Hello {username}! Access granted."}