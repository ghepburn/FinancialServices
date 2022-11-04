from flask import Response

def CatchModelErrors(func):

    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            errorMessage = "Model error " + str(func) + ": " + str(e)
            print(errorMessage)
            raise Exception(str(e))

    return wrap
