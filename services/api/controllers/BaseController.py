from services.api import db
from flask import Response

from .decorators.CatchErrors import CatchErrors

class BaseController:

    def __init__(self):
        pass
    
    @CatchErrors
    def getAll(self):
        data = self.model.query.all()

        response = {}
        for item in data:
            dic = item.toDict()
            response[dic["id"]] = dic

        return response
    
    @CatchErrors
    def getById(self, id):
        data = self.model.query.filter_by(id=id)

        noModelFound = data.count() == 0
        if noModelFound:
            data = self.model.query.filter_by(ref_num=id)

        noModelFound = data.count() == 0
        if noModelFound:
            return Response("No model with id: " + id, 400)
        
        model = data[0]
        
        return model.toDict()

    @CatchErrors
    def create(self, data):
        model = self.model(**data)

        db.session.add(model)
        db.session.commit()

        return model.toDict()

    @CatchErrors
    def update(self, id, data):
        models = self.model.query.filter_by(id=id)

        noModelFound = models.count() == 0
        if noModelFound:
            return Response("No model with id: " + id, 400)

        model = models.first()

        self.setRefnum(data)

        for key in data.keys():
            setattr(model, key, data[key])
        
        db.session.add(model)
        db.session.commit()

        return model.toDict()

    @CatchErrors
    def delete(self, id):
        models = self.model.query.filter_by(id=id) 

        noModelFound = models.count() == 0
        if noModelFound:
            return Response("No model with id: " + id, 400)

        model = models.first()

        db.session.delete(model)
        db.session.commit()

        return {}

    @CatchErrors
    def setRefnum(self, data):
        data["ref_num"] = data["name"]
        return data