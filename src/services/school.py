from src.db.school_student import SchoolCrud


class SchoolService:

    @classmethod
    def create_school(cls, school_req, session):
        return SchoolCrud.create_school(
            school_req,
            session
        )