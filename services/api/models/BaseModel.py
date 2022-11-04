# A "Base Model" class
# Who is intended to provide methods to all models

from .decorators.CatchModelErrors import CatchModelErrors
from .etl.ModelTransformer import ModelTransformer
class BaseModel(object):
    transformer = ModelTransformer()

    def __init__(self, **kwargs):

        kwargs = self.cleanData(kwargs)

        super().__init__(**kwargs)   
        self.setReferenceNumber() 

    def __repr__(self):
        return self.ref_num

    @CatchModelErrors
    def toDict(self):
        dic = {}

        for col in self.__table__.columns:
            dic[col.name] = getattr(self, col.name)

        return dic

    @CatchModelErrors
    def setReferenceNumber(self):
        self.ref_num = self.name

    @CatchModelErrors
    def cleanData(self, data: dict):
        for key in data.keys():

            if "date" in key:
                data[key] = self.transformer.transformDate(data[key])

        return data