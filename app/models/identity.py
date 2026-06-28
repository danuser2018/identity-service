from pydantic import BaseModel

class Identity(BaseModel):
    name: str
    email: str

class NameResponse(BaseModel):
    name: str

class EmailResponse(BaseModel):
    email: str

class HealthResponse(BaseModel):
    status: str
