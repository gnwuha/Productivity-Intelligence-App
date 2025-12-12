from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Task
from datetime import datetime, timezone

router = APIRouter()

#getting all tasks
@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

#POST request creating a new task
@router.post("/tasks")
def create_task(title: str, 
                category: str = None,
                description: str = None,
                due_date: datetime = None,
                estimated_duration: int = None,
                estimated_effort: int = None,
                db: Session = Depends(get_db)):
    #creates, adds new task to session, finalizing it, 
    #and refreshes obj for auto-generated fields, it
    new_task = Task(title = title, category=category, description=description, due_date=due_date, estimated_duration=estimated_duration, estimated_effort=estimated_effort)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task #for confirmation

#PUT request, changing a task's status to completion
@router.put("/tasks/{task_id}/complete")
def complete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return {"error": "Task not found"}
    
    task.status = "Completed"
    task.completed_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(task)
    return task

@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    title: str = None,
    category: str = None,
    description: str = None,
    due_date: datetime = None,
    status: str = None,
    priority: str = None,
    estimated_duration: int = None,
    estimated_effort: int = None,
    db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return {"error": "Task not found"}
    
    if title is not None:
        task.title = title
    if category is not None:
        task.category = category
    if description is not None:
        task.description = description
    if due_date is not None:
        task.due_date = due_date
    if status is not None:
        task.status = status
    if priority is not None:
        task.priority = priority
    if estimated_duration is not None:
        task.estimated_duration = estimated_duration
    if estimated_effort is not None:
        task.estimated_effort = estimated_effort

        
    db.commit()
    db.refresh(task)
    return task
    

#DELETE request
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return {"error": "Task not found"}
    db.delete(task)
    db.commit()
    return {"message": f"Task {task_id} deleted successfully"}