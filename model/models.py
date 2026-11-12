from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import func
from sqlalchemy.orm import relationship

# =====================================

from app.databse import Base

# =====================================

class Cana_system(Base):
    __tablename__ = "cana"

    id = Column(Integer, primary_key = True, autoincrement = True)
    letter = Column(String, nullable = False)
    romaji = Column(String, nullable = False)
    translate = Column(String, nullable = False)

class Vocabulary(Base):
    __tablename__ = "vocab"

    id = Column(Integer, primary_key = True, autoincrement = True)
    words = Column(String, nullable = False)
    romaji = Column(String, nullable = False)
    translate = Column(String, nullable = False)