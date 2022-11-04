

class BaseModelMixin(object):
    def __repr__(self):
        return self.ref_num

    def toDict(self):
        dic = {}

        for col in self.__table__.columns:
            dic[col.name] = getattr(self, col.name)

        return dic
    
    def isModel(self):
        return True