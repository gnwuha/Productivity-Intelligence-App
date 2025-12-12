#imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#location for database file and creating the engine (allowing multiple threads)
SQLALCHEMY_DATABASE_URL = "sqlite:///./productivity.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=
                       {"check_same_thread": False})

#producing database session creation to interact with database
#changes made shouldn't be finalized until user says so
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

#classes like users and tasks will inherit this later for database properties
Base = declarative_base()

#dependency for creating and closing database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()        
