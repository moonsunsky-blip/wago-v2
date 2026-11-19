import os
import sqlite3

from app.database import engine, SessionLocal
import model.letter_models as models

# ============================================

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# ============================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "data", "japanese_N5.db")

HIRAGANA = os.path.join(BASE_DIR, "data", "hiragana.txt")

# ============================================

def pirsing(file_read):
    read_list = []

    with open(file_read, "r", encoding = "utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue
            parts = [p.strip() for p in line.split("|")]

            if len(parts) == 4:
                kanji_obj = models.Kanji(
                    letter = parts[0],
                    onyomi=parts[1],
                    kunyomi=parts[2],
                    meaning=parts[3]
                )
                read_list.append(kanji_obj)

    return read_list



# ============================================

def seed_kanji():
    db = SessionLocal()

    try:
        dir_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(dir_path, "data", "txt_data", "kanji.txt")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"file not found: {file_path}")

        kanji_list = pirsing(file_path)

        db.add_all(kanji_list)
        db.commit()
        print("done!")

    except Exception as e:
        db.rollback()
        print(f"error ... : {e}")
    finally:
        db.close()
        

    


# ============================================


if __name__ == "__main__":
    
    seed_kanji()
   
    check_db = SessionLocal()
    count = check_db.query(models.Kanji).count()
    print(f"session in cana {count} .")
    check_db.close()
    db.close()