from services.dataImporter.maps.bmoChequingsTransactionMap import bmoChequingsTransactionMap
from services.dataImporter.maps.bmoCreditCardTransactionMap import bmoCreditCardTransactionMap

class Transformer:
    
    def __init__(self, logger=None):
        self.logger=logger
        self.dataMap = []

    def transform(self, data):
        self.log("Transformed")
        return data

    def log(self, msg):
        self.logger.log(self.__class__.__name__, msg)

    def getMap(self, dataSource):
        options = {
            "bmoChequings": bmoChequingsTransactionMap,
            "bmoCreditcard": bmoCreditCardTransactionMap
        }

        return options[dataSource]