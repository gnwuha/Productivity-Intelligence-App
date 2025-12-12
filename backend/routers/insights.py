from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Insight 

router = APIRouter()

@router.post("/insights")
def create_insight(content: str,
                   insight_type: str = "productivity",
                   db: Session = Depends(get_db)):
    new_insight = Insight(insight_type=insight_type, content=content)
    db.add(new_insight)
    db.commit()
    db.refresh(new_insight)
    return new_insight
    
@router.get("/insights")
def get_insights(db: Session = Depends(get_db)):
    insights = db.query(Insight).all()
    return insights

@router.delete("/insights/{insight_id}")
def delete_insight(insight_id: int, db: Session = Depends(get_db)):
    insight = db.query(Insight).filter(Insight.id == insight_id).first()
    if not insight:
        return {"error": "Insight not found"}
    db.delete(insight)
    db.commit()
    return {"message": f"Insight {insight_id} delete successfully"}