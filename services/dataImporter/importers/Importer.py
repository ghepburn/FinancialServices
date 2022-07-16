from services.dataImporter.loggers.Logger import Logger
from services.dataImporter.iterators.Iterator import Iterator
from services.dataImporter.validators.Validator import Validator
from services.dataImporter.transformers.Transformer import Transformer
from services.dataImporter.loaders.Loader import Loader
from services.dataImporter.synchronizers.Synchronizer import Synchronizer

class Importer:
    logger = Logger()
    iterator = Iterator
    validator = Validator
    transformer = Transformer
    loader = Loader
    synchronizer = Synchronizer
    
    def __init__(self, importConfigs):
        self.configs = importConfigs
        self.logger.setOutputLocation(self.configs.get("logOutputPath"))
        
        self.log("Initialized")

    def run(self):

        data = self.getData()

        synchronizer = self.synchronizer(self.logger, self.iterator, self.validator, self.transformer, self.loader)
  
        results = synchronizer.synch(data)

        self.log("Import Completed. Resulting Row Count: " + str(len(results)))

        self.log(results[-5:-1])

        return results

    def getData(self):
        return [["a", "b", "c"], ["d", "e", "f"]]

    # Support file naming convetion of {source}_{startDate}_{endDate}.xxx
    def getDataSource(self, filePath):
        fileName = filePath.split("/")[-1]
        fileNameParts = fileName.split("_")
        source = fileNameParts[0]

        return source

    def log(self, msg):
        self.logger.log(self.__class__.__name__, msg)
        