from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserInDB(UserBase):
    hashed_password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
