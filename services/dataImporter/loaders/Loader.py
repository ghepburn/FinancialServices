class Loader:
    
    def __init__(self, logger=None):
        self.logger=logger

    def load(self, data):
        self.log("Loading")
        self.log("Loaded")
        return data

    def log(self, msg):
        self.logger.log(self.__class__.__name__, msg)