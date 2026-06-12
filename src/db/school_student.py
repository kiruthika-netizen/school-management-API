from src.models.school import School
from src.models.student import Student


class SchoolStudentCrud:

    @classmethod
    def save(cls, obj, db):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @classmethod
    def create_school(cls, school_req, db):
        school = School(
            school_name=school_req.school_name
        )
        return cls.save(school, db)

    @classmethod
    def create_student(cls, student_req, db):
        student = Student(
            student_name=student_req.student_name,
            age=student_req.age,
            school_id=student_req.school_id
        )
        return cls.save(student, db)