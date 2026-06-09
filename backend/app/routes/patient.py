from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.models import Patient

from app.schemas.patient_schema import (
    PatientCreate,
    PatientResponse
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)

@router.post("/", response_model=PatientResponse)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):

    new_patient = Patient(
        name=patient.name,
        age=patient.age,
        condition=patient.condition
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient

@router.get("/", response_model=list[PatientResponse])
def get_patients(
    db: Session = Depends(get_db)
):

    return db.query(Patient).all()

@router.get("/{patient_id}",
            response_model=PatientResponse)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient

@router.put("/{patient_id}",
            response_model=PatientResponse)
def update_patient(
    patient_id: int,
    updated_patient: PatientCreate,
    db: Session = Depends(get_db)
):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    patient.name = updated_patient.name
    patient.age = updated_patient.age
    patient.condition = updated_patient.condition

    db.commit()
    db.refresh(patient)

    return patient

@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    db.delete(patient)
    db.commit()

    return {
        "message": "Patient deleted"
    }

