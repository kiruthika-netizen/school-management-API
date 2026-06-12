from src.db.school_student import StudentCrud


class StudentService:

    @classmethod
    def create_student(cls, student_req, session):
        return StudentCrud.create_student(
            student_req,
            session
        )