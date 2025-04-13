from pydantic import BaseModel

class Robot(BaseModel):
    id: int
    name: str
    status: str

