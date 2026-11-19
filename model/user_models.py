from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

# =====================================

from app.database import Base

# =====================================

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True, autoincrement = True)
    email = Column(String, unique = True, index = True, nullable = False)
    hashed_password = Column(String, nullable = False)
    is_active = Column(Boolean, default = True)
    is_premium = Column(Boolean, default = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    user_level = Column(String, default = "begginer")

# =====================================
# this for future...
# =====================================
class UserNote(Base):
    __tablename__ = "user_note"

    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String, nullable = False)
    content = Column(Text, nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())

    #user_id
    user_id = Column(Integer, ForeignKey("user.id"), nullable = False)

    #author of note ....
    