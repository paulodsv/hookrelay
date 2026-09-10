from pydantic import BaseModel

class CreateDestination(BaseModel):
    name: str
    url: str