from services.api import db

class BaseModel(db.Model):

    def toDict(self):
        dic = {}

        for col in self.__table__.columns:
            dic[col.name] = getattr(self, col.name)

        return dic

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return self.ref_num
