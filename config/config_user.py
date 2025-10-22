from fastapi import HTTPException,status
from config.pass_hashing import pwd_context
from db.users import USER_DATA
from models import UserInDB

def register_user(username: str, password: str):
    for user in USER_DATA:
        if user.username == username:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    
    hashed_password = pwd_context.hash(password)
    
    new_user = UserInDB(username=username, hashed_password=hashed_password)

    USER_DATA.append(new_user)

    return {"message": f"User {username} successfully created!"}


def authenticate_user(username: str, password: str) -> bool:
    for user in USER_DATA:
        if user.username == username and pwd_context.verify(password, user.hashed_password):
            return True

    return False