from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.db import engine
from app.database.models import Base

from app.routes.auth import router as auth_router
from app.routes.patient import router as patient_router
from app.routes.exercise import router as exercise_router
from app.routes.analysis import router as analysis_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(patient_router)
app.include_router(exercise_router)
app.include_router(analysis_router)

@app.get("/")
def root():
    return {"message": "AR Physiotherapy API Running"}
