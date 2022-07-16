import json

class BaseController:

    def __init__(self):
        pass

    def getAll(self):
        data = self.model.query.all()
        return self.response(data)
    
    def getById(self, id):
        data = self.model.query.filter_by(id=id)
        return self.response(data)

    def response(self, data):

        response = {}

        for item in data:
            dic = item.toDict()
            response[dic["id"]] = dic

        return response