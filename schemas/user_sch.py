# ====================================

from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime

# ====================================

class UserCreate(BaseModel):

    email: EmailStr
    password: str

class UserResponse(BaseModel):

    id: int
    email: EmailStr
    is_active: bool
    is_premium: bool
    created_at: datetime
    user_level: str

    model_config = ConfigDict(from_attributes = True)

# ====================================
# user tokens
# ====================================

class Token(BaseModel):

    access_token: str
    token_type: str = "bearer"

# ==================================== 
# ====================================

# user note

class NoteCreate(BaseModel):

    title: str
    content: str

class NoteResponse(BaseModel):

    id: int
    title: str
    content: str
    created_at: datetime
    user_id: int

    model_config = ConfigDict(from_attributes = True)