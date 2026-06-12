from src.db.school_student import SchoolStudentCrud


class StudentService:

    @classmethod
    def create_student(cls, student_req, session):
        return SchoolStudentCrud.create_student(
            student_req,
            session
        )