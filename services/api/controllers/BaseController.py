from services.api import db
from flask import Response
from sqlalchemy import or_

from .decorators.CatchErrors import CatchErrors

class BaseController:

    def __init__(self):
        pass
    
    @CatchErrors
    def getAll(self):
        models = self.model.query.all()

        response = {}
        for item in models:
            dic = item.toDict()
            response[dic["id"]] = dic

        return response
    
    @CatchErrors
    def getById(self, id):
        models = self.model.query.filter(or_(self.model.id==id, self.model.ref_num==id))

        noModelFound = models.count() == 0
        if noModelFound:
            return Response("No model with id: " + id, 400)
        
        model = models[0]
        
        return model.toDict()

    @CatchErrors
    def create(self, data):
        model = self.model(**data)

        db.session.add(model)
        db.session.commit()

        return model.toDict()

    @CatchErrors
    def bulkCreate(self, data):
        models = {}
        count = 0
        for item in data:
            count += 1
            model = self.create(item)
            models[count] = model

        return models

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