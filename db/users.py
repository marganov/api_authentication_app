from models import UserInDB
from config.pass_hashing import get_password_hash

USER_DATA: list[UserInDB] = [
    UserInDB(username="user1", hashed_password=get_password_hash("pass1"))
]