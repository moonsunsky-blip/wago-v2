import os
import sqlite3

from app.databse import engine, SessionLocal
import model.letter_models as models

# ============================================

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# ============================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "data", "japanese_N5.db")

HIRAGANA = os.path.join(BASE_DIR, "data", "hiragana.txt")

# ============================================

def parse_with_model(file_read, alphabet_type="hiragana"):
    read_list = []

    with open(file_read, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue
            parts = [p.strip() for p in line.split("|")]

            if len(parts) == 3:
                hiragana = models.CanaSystem(
                    letter=parts[0],
                    romaji=parts[1],
                    translate=parts[2],
                    type=alphabet_type
                )
                read_list.append(hiragana)

    return read_list

def seed():
    db_session = SessionLocal() 

    print("load....")

    try:
        current_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_path, "data", "txt_data", "hiragana.txt")

        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"file not found: {file_path}")

        
        clean_path = os.path.abspath(file_path)

        hiragana_objects = parse_with_model(clean_path, alphabet_type="hiragana")

        
        db_session.add_all(hiragana_objects)
        db_session.commit()
        print("done!")

    except Exception as e:
        db_session.rollback()
        print(f"error ... : {e}")
    finally:
        db_session.close()

# ============================================
def main_init():
    print("load init ...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT (*) FROM canasystems")
    pass

if __name__ == "__main__":
    seed()
    
   
    check_db = SessionLocal()
    count = check_db.query(models.CanaSystem).count()
    print(f"session in cana {count} .")
    check_db.close()
    db.close()