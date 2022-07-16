import os

from services.dataImporter.importers.CsvImporter import CsvImporter

def importCsvFiles(configs):

    importer = CsvImporter(configs)
    importer.run()