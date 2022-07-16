
class Synchronizer:
    
    def __init__(self, logger, iterator, validator, transformer, loader):
        self.logger = logger
        self.iterator = iterator(self.logger)
        self.validator = validator(self.logger)
        self.transformer = transformer(self.logger)
        self.loader = loader(self.logger)

    def synch(self, data):
        results = []

        self.log("Synch Starting")

        self.iterator.setData(data)

        while self.iterator.hasNext():
            batch = self.iterator.getNext()

            for i in range(len(batch)):
                item = batch[i]

                try:
                    valdiatedBatch = self.validator.validate(item)
                except Exception as error:
                    self.log("Error: Batch ->")
                    self.log(item)
                    self.log(error)

                try:
                    transformedBatch = self.transformer.transform(valdiatedBatch)
                except Exception as error:
                    self.log("Error: Validated Batch ->")
                    self.log(valdiatedBatch)
                    self.log(error)

                try:
                    loadedBatch = self.loader.load(transformedBatch)
                except Exception as error:
                    self.log("Error: Transformed Batch ->")
                    self.log(transformedBatch)
                    self.log(error)

                results.append(loadedBatch)

        self.log("Synch Completed")

        return results

    def log(self, msg):
        self.logger.log(self.__class__.__name__, msg)

