from fastapi import APIRouter

router = APIRouter(prefix="/exercise", tags=["exercise"])

@router.get("/")
def get_exercises():
    pass

@router.post("/")
def create_exercise():
    pass
