import os

from services import dataImporter

if __name__ == '__main__':

    cwd = os.getcwd()

    instructions = {
        "filePath": cwd + "/data/",
        "fileName":"bmoChequings_jan012022_july052022.csv",
        # "logOutputPath": cwd + "/services/dataImporter/logs/"
    }

    dataImporter.importCsvFiles(instructions)