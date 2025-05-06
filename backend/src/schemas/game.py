from pydantic import BaseModel

class HintOut(BaseModel):
    word: str
    distance: float
    x: float
    y: float


class GuessOut(BaseModel):
    guess: str
    distance: float
    x: float
    y: float
    correct: bool
