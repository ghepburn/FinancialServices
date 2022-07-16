class Transformer:
    
    def __init__(self, logger=None):
        self.logger=logger

    def transform(self, data):
        self.log("Transforming")
        self.log("Transformed")
        return data

    def log(self, msg):
        self.logger.log(self.__class__.__name__, msg)