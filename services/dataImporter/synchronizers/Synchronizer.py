from services.dataImporter.maps.TransactionMap import TransactionMap

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

        count = 0
        while self.iterator.hasNext():
            batch = self.iterator.getNext()
            count += 1

            if count == 1:
                headers = self.getHeaders(batch)
                dataMap = TransactionMap(headers)
                self.setDataMap(dataMap)
                continue

            for i in range(len(batch)):
                item = batch[i]

                try:
                    valdiatedBatch = self.validator.validate(item)
                except Exception as error:
                    self.log("Validation Failed.")
                    self.log("Error: Batch ->")
                    self.log(item)
                    self.log(error)

                try:
                    transformedBatch = self.transformer.transform(valdiatedBatch)
                except Exception as error:
                    self.log("Transformation failed.")
                    # continue
                    self.log("Error: Validated Batch ->")
                    self.log(valdiatedBatch)
                    self.log("Error transforming batch.")
                    self.log(error)

                try:
                    loadedBatch = self.loader.load(transformedBatch)
                except Exception as error:
                    self.log('Loading failed.')
                    continue
                    self.log("Error: Transformed Batch ->")
                    self.log(transformedBatch)
                    self.log(error)

                results.append(loadedBatch)

        self.log("Synch Completed")

        return results

    def log(self, msg):
        self.logger.log(self.__class__.__name__, msg)

    def setDataMap(self, dataMap):
        self.validator.dataMap = dataMap
        self.transformer.dataMap = dataMap

    def getHeaders(self, batch):
        numOfItemsInBatch = self.iterator.batchSize

        if numOfItemsInBatch == 1:
            return batch
        else:
            return batch[0]

