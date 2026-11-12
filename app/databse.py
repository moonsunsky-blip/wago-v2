import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker



APP = os.path.abspath.dirname(os.path.abspath(__file__))
BASEDIR = os.path.dirname(APP)
PATH = os.path.join(BASEDIR, "data", "japanese_N5.db")


clean_path = os.path.abspath(PATH).replace('\\', '/')

engine = create_engine(
    f"sqlite:///{clean_path}", connect_args = {"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass