from pydantic import BaseModel

class ExerciseCreate(BaseModel):
    exercise_type: str
    patient_id: int

class ExerciseOut(BaseModel):
    id: int
    exercise_type: str
    score: float

    class Config:
        from_attributes = True
