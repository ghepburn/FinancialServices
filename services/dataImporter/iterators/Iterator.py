from asyncio.log import logger


class Iterator:
    batchSize = 1
    data = []

    def __init__(self, logger=None):
        self.logger = logger

    def log(self, msg):
        self.logger.log(self.__class__.__name__, msg)

    def setData(self, data):
        self.data = self.standardizeData(data)
        self.log('Data Set')
        
    def standardizeData(self, data):
        data.reverse()
        return data

    def getNext(self, count=1):
        result = []
        for i in range(count):
            item = self.data.pop()
            result.append(item)
        return result

    def hasNext(self):
        return len(self.data) > 0