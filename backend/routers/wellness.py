from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import WellnessCheck
from datetime import datetime, timezone

router = APIRouter()

@router.get("/wellness-checks")
def get_wellness_checks(db: Session = Depends(get_db)):
    wellness_checks = db.query(WellnessCheck).all()
    return wellness_checks

@router.post("/wellness-checks")
def create_wellness_check(mood: int,
                          energy_level: int,
                          stress_level: int,
                          notes: str = None,
                          db: Session = Depends(get_db)):
    new_wellness_check = WellnessCheck(mood=mood, energy_level=energy_level, stress_level=stress_level, notes=notes)
    db.add(new_wellness_check)
    db.commit()
    db.refresh(new_wellness_check)
    return new_wellness_check

@router.put("/wellness-checks/{check_id}")
def update_wellness_check(
    check_id: int,
    mood: int = None,
    energy_level: int = None,
    stress_level: int = None,
    notes: str = None,
    db: Session = Depends(get_db)
    ):
    
    wellness_check = db.query(WellnessCheck).filter(WellnessCheck.id == check_id).first()
    if not wellness_check:
        return {"error": "Wellness check not found"}
    
    if mood is not None:
        wellness_check.mood = mood
    if energy_level is not None:
        wellness_check.energy_level = energy_level
    if stress_level is not None:
        wellness_check.stress_level = stress_level
    if notes is not None:
        wellness_check.notes = notes
    
    db.commit()
    db.refresh(wellness_check)
    return wellness_check

@router.delete("/wellness-checks/{check_id}")
def delete_wellness_checks(check_id: int, db: Session = Depends(get_db)):
    wellness_check = db.query(WellnessCheck).filter(WellnessCheck.id == check_id).first()
    if not wellness_check:
        return {"error": "Wellness check not found"}
    
    db.delete(wellness_check)
    db.commit()
    return {"message": f"Wellness check {check_id} deleted successfully"}

