from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import tasks, wellness, analytics, insights, ai_insights

#app and databse creation
app = FastAPI(title= "Productivity AI API")
Base.metadata.create_all(bind=engine)

#CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#home page test
@app.get("/")
def root():
    return{"message": "Productivity app is running"}

app.include_router(tasks.router)
app.include_router(wellness.router)
app.include_router(analytics.router)
app.include_router(insights.router)
app.include_router(ai_insights.router)