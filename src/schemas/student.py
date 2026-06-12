from pydantic import Field
from src.schemas.base import PydanticBaseModel


class StudentCreate(PydanticBaseModel):
    name: str = Field(..., description="Student Name")
    age: int = Field(..., description="Student Age")
    school_id: int = Field(..., description="School ID")