from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.base import Base


class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    school_name = Column(String)

    students = relationship(
        "Student",
        back_populates="school"
    )