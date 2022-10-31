class Validator:
    
    def __init__(self, logger=None):
        self.logger = logger
        self.dataMap = []

    def validate(self, data):
        self.log("Validated")
        return data

    def log(self, msg):
        self.logger.log(self.__class__.__name__, msg)