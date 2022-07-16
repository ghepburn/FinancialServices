import os
from datetime import datetime
import json

class Logger:
    method = print
    directory = str(datetime.today()).split(" ")[0] + "/"
    fileName = "dataImport_" + str(datetime.timestamp(datetime.now())) + ".txt"
    location = ""

    def log(self, location, msg):

        if type(msg) == str:
            output = self.__class__.__name__.upper() + ": " + location + " -> " + msg
        else:
            output = json.dumps(msg)

        method = self.getMethod()
        method(output)

    def getMethod(self):
        return self.method

    def setOutputLocation(self, path):
        if path:
            os.chdir(path)
            try:
                os.mkdir(self.directory)
            except Exception as error:
                pass

            self.location = path + self.directory + self.fileName
            self.method = self.printToFile
            print(self.__class__.__name__.upper() + "-> " + "logging to " + self.location)

    def printToFile(self, output):
        file = open(self.location, "a")
        file.write(output + "\n")
        file.close()