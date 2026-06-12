from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.schemas.school import SchoolCreate
from src.services.school import SchoolService

router = APIRouter()


@router.post(
    "/school",
    summary="Add School"
)
def create_school(
    school_req: SchoolCreate = Body(description=""),
    session: Session = Depends(get_db)
):

    school = SchoolService.create_school(
        school_req,
        session
    )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": "School created successfully",
            "data": {
                "id": school.id,
                "school_name": school.school_name
            }
        }
    )