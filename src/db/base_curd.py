class BaseCrud:

    @classmethod
    def save(cls, obj, db):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj