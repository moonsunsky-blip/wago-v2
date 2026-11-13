# ====================================

from pydantic import BaseModel, ConfigDict

# ====================================

class CanaSystem(BaseModel):

    id:int
    letter: str
    romaji: str
    translate: str
    type: str

    model_config = ConfigDict(from_attributes = True)

class VocabRsponse(BaseModel):

    id: int
    words: str
    romaji: str
    translate: str

    model_config = ConfigDict(from_attributes = True)

class KanjiResponse(BaseModel):

    id: int
    letter: str
    onyomi: str
    kunyomi: str
    meaning: str

    model_config = ConfigDict(from_attributes = True)

class GrammarResponse(BaseModel):

    id: int
    title: str
    category: str
    structure: str
    meaning: str
    explation: str

    model_config = ConfigDict(from_attributes = True)

