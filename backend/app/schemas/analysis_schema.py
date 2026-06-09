from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    angle: float
    rep_count: int
    feedback: str
    status: str