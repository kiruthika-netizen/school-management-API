from pydantic import Field
from src.schemas.base import PydanticBaseModel


class SchoolCreate(PydanticBaseModel):
    school_name: str = Field(..., description="School Name")