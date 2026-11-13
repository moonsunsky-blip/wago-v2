from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import func
from sqlalchemy.orm import relationship

# =====================================

from app.databse import Base

# =====================================

class CanaSystem(Base):
    __tablename__ = "cana"

    id = Column(Integer, primary_key = True, autoincrement = True)
    letter = Column(String, nullable = False)
    romaji = Column(String, nullable = False)
    translate = Column(String, nullable = False)
    type = Column(String, nullable = False)

class Vocabulary(Base):
    __tablename__ = "vocab"

    id = Column(Integer, primary_key = True, autoincrement = True)
    words = Column(String, nullable = False)
    romaji = Column(String, nullable = False)
    translate = Column(String, nullable = False)

class Kanji(Base):
    __tablename__ = "kanji"

    id = Column(Integer, primary_key = True, autoincrement = True)
    letter = Column(String, nullable = False)
    onyomi = Column(String)
    kunyomi = Column(String)
    meaning = Column(String, nullable = False)

class Grammar(Base):
    __tablename__ = "grammar"

    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String, nullable = False)
    category = Column(String, nullable = False)
    structure = Column(String, nullable = False)
    meaning = Column(String, nullable = False)
    explanation = Column(Text, nullable = False)
    