from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    
    #identifying and info
    title = Column(String, index=True, nullable=False)
    category = Column(String)
    description = Column(String)
    
    #time
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    completed_at = Column(DateTime)
    due_date = Column(DateTime)
    status = Column(String, default="Not Started")
    
    priority = Column(String, default="medium")
    
    #user expectations and emotions
    estimated_duration = Column(Integer)
    actual_duration = Column(Integer, nullable= True)
    estimated_effort = Column(Integer)
    user_feeling = Column(Integer, nullable=True)
    
class WellnessCheck(Base):
    __tablename__ = "wellness_checks"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    mood = Column(Integer)
    energy_level = Column(Integer)
    stress_level = Column(Integer)
    notes = Column(String)
    
class Insight(Base):
    __tablename__ = "insights"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    insight_type = Column(String)
    content = Column(String)
    dismissed = Column(Integer, default=0)
    

        
