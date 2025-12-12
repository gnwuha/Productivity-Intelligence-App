from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Task, WellnessCheck
from datetime import datetime, timezone, timedelta

router = APIRouter()

@router.get("/analytics")
def get_analytics(db: Session = Depends(get_db)):
    total_tasks = db.query(Task).count()
    completed_tasks = db.query(Task).filter(Task.status == "Completed").count()
    pending_tasks = db.query(Task).filter(Task.status == "Not Started").count()
    
    #Wellness statistics
    #Using periodic averages to better understand user's mood
    #mood, energy, and stress allow for a deeper understanding of one's mental wellbeing 
    wellness_checks = db.query(WellnessCheck).all()
    seven_days_ago = datetime.now(timezone.utc) - timedelta(days=7)
    recent_checks = db.query(WellnessCheck).filter(WellnessCheck.timestamp >= seven_days_ago).all()
    
    if wellness_checks:
        avg_mood = sum(w.mood for w in wellness_checks)/ len(wellness_checks)
        avg_energy = sum(w.energy_level for w in wellness_checks) / len(wellness_checks)
        avg_stress = sum(w.stress_level for w in wellness_checks) / len(wellness_checks)
    else:
        avg_mood = avg_energy = avg_stress = 0
        
    if recent_checks:
        recent_avg_mood = sum(w.mood for w in recent_checks)/len(recent_checks)
        recent_avg_energy = sum(w.energy_level for w in recent_checks)/len(recent_checks)
        recent_avg_stress = sum(w.stress_level for w in recent_checks)/len(recent_checks)
    else:
        recent_avg_mood = recent_avg_energy = recent_avg_stress = 0
        
    return {
        "tasks":{
            "total": total_tasks,
            "completed": completed_tasks,
            "pending": pending_tasks
        },
        "wellness": {
            "average_mood_level": round(avg_mood, 2),
            "average_energy_level": round(avg_energy, 2),
            "average_stress_level": round(avg_stress, 2)
        },
        "last_seven_days": {
            "average_mood_level": round(recent_avg_mood, 2),
            "average_energy_level": round(recent_avg_energy, 2),
            "average_stress_level": round(recent_avg_stress, 2)
        }
    }