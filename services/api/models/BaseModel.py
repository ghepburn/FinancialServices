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
    def getForeignKeys(self):
        foreignKeys = []
        for col in self.__table__.columns:
            for key in col.foreign_keys:
                print(key)

    @CatchModelErrors
    def cleanData(self, model: dict):
        for key in model.keys():

            if "date" in key:
                model[key] = self.transformer.transformDate(model[key])

            self.getForeignKeys()

        return model