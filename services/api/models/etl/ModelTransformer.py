from datetime import datetime

class ModelTransformer():

    def transformDate(self, value):
        try:
            date = datetime.strptime(value, "%Y-%m-%d")
            date = date.date()
            return date
        except:
            errorMessage = "Dates must be formated as 'YYYY-MM-DD'"
            print(errorMessage)
            raise Exception(errorMessage)