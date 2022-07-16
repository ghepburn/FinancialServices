import csv
import os

from services.dataImporter.importers.Importer import Importer
from services.dataImporter.loggers.Logger import Logger
from services.dataImporter.iterators.CsvIterator import CsvIterator
from services.dataImporter.validators.Validator import Validator
from services.dataImporter.transformers.TransactionTransformer import TransactionTransformer
from services.dataImporter.loaders.Loader import Loader

class CsvImporter(Importer):

    transformer = TransactionTransformer
    
    def getData(self):
        self.log("Getting Data")

        data = []
        
        filePath = self.configs["filePath"]
        fileName = self.configs.get("fileName")

        if fileName is None:
            data = self.getDataFromFiles(filePath)
        else:
            data = self.getDataFromFile(data, filePath + fileName)

        self.log("Retrieved Data. Row Count: " + str(len(data)))

        return data

    def getDataFromFiles(self, path):
        data = []
        files = os.listdir(path)

        for file in files:
            filePath = path + file
            isFile = os.path.isfile(filePath)

            if not isFile:
                break
                
            data = self.getDataFromFile(data, filePath)
        return data

    def getDataFromFile(self, data, filePath):

        dataSource = self.getDataSource(filePath)

        try:
            with open(filePath) as file:
                csvFile = csv.reader(file)

                for row in csvFile:
                    row.append(dataSource)
                    data.append(row)
        except Exception as error:
            self.log("Error getting data from " + filePath)
            self.log(error)

        return data