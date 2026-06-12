from src.db.school_student import SchoolStudentCrud


class SchoolService:

    @classmethod
    def create_school(cls, school_req, session):
        return SchoolStudentCrud.create_school(
            school_req,
            session
        )