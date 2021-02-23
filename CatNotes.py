from pydantic import BaseModel


class CatNotes(BaseModel):
    name: str
#   category: str
