import os
from services import dataImporter

if __name__ == '__main__':

    instructions = {
        "filePath":os.getcwd() + "/data/"
        # "fileName":"test.csv"
    }

    dataImporter.importCsvFiles(instructions)