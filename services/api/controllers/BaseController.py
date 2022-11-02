from services.api import db

class BaseController:

    def __init__(self):
        pass

    def getAll(self):
        data = self.model.query.all()
        return self.response(data)
    
    def getById(self, id):
        data = self.model.query.filter_by(id=id)

        noModelFound = data.count() == 0
        if noModelFound:
            data = self.model.query.filter_by(ref_num=id)
        
        return self.response(data)

    def create(self, data):
        if "ref_num" not in data.keys():
            data = self.setRefnum(data)

        model = self.model(**data)
        db.session.add(model)
        db.session.commit()

        return self.response(model)

    def update(self, id, data):
        models = self.model.query.filter_by(id=id)

        noExistingModel = models.count() == 0
        if noExistingModel:
            errorMessage = "Id " + id + " does not exist."
            return self.errorResponse(errorMessage, 400)

        model = models.first()

        self.setRefnum(data)

        for key in data.keys():
            setattr(model, key, data[key])
        
        db.session.add(model)
        db.session.commit()

        return self.response(model)

    def delete(self, id):
        return False

    def setRefnum(self, data):
        data["ref_num"] = data["name"]
        return data

    def response(self, data):
        response = {}

        if type(data) == "object":
            response = data.toDict()
        else:
            for item in data:
                dic = item.toDict()
                response[dic["id"]] = dic

        return response

    def errorResponse(self, message, errorCode=500):
        response = {}
        response["errorCode"] = errorCode
        response["message"] = message

        return response