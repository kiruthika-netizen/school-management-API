from fastapi import FastAPI

from src.api.school import router as school_router
from src.api.student import router as student_router

from src.db.base import Base
from src.db.session import engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(school_router)
app.include_router(student_router)