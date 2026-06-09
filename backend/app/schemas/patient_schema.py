from pydantic import BaseModel

class PatientCreate(BaseModel):
    name: str
    age: int
    condition: str


class PatientResponse(PatientCreate):
    id: int

    class Config:
        from_attributes = True