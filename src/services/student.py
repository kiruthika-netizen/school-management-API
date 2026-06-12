from src.models.student import Student


class StudentService:

    @classmethod
    def create_student(cls, student_req, db):

        student = Student(
            name=student_req.name,
            age=student_req.age,
            school_id=student_req.school_id
        )

        db.add(student)
        db.commit()
        db.refresh(student)

        return student