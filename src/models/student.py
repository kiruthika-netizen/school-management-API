from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db.base import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String)
    age = Column(Integer)

    school_id = Column(Integer, ForeignKey("schools.id"))

    school = relationship("School", back_populates="students")