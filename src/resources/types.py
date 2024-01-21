from typing import List
from pydantic import BaseModel



class Text(BaseModel):
    text: str
    language: str

class Speech(BaseModel):
    amplitudes: List[float]