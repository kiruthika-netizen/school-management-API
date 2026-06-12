from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.schemas.student import StudentCreate
from src.services.student import StudentService

router = APIRouter()


@router.post(
    "/student",
    summary="Add Student"
)
def create_student(
    student_req: StudentCreate = Body(description=""),
    session: Session = Depends(get_db)
):

    student = StudentService.create_student(
        student_req,
        session
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": "Student created successfully",
            "data": {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "school_id": student.school_id
            }
        }
    )