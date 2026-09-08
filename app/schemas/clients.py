from pydantic import BaseModel

class CreateClient(BaseModel):
    name: str