from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Task, WellnessCheck, Insight
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
router = APIRouter()

@router.post("/generate-insight")
def generate_insight(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    wellness_checks = db.query(WellnessCheck).all()
    
    prompt = f"""
    You are a productivity coach. Analyze this user's data and provide personalized insight:
    
    Tasks: {len(tasks)} total
    Completed: {len([t for t in tasks if t.status == 'Completed'])}
    
    Recent wellness (last 3 checks):
    {[f"Mood: {w.mood}, Energy: {w.energy_level}, Stress: {w.stress_level}" for w in wellness_checks[-3:]]}
    
    Provide a brief, encouraging insight about their productivity and wellness patterns.
    """
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    new_insight = Insight(content = response.text, insight_type="productiviity")
    db.add(new_insight)
    db.commit()
    db.refresh(new_insight)
    
    return new_insight