from src.models.school import School


class SchoolService:

    @classmethod
    def create_school(cls, school_req, db):

        school = School(
            school_name=school_req.school_name
        )

        db.add(school)
        db.commit()
        db.refresh(school)

        return school