from flask import Response

def CatchErrors(func):

    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            errorMessage = "Controller error " + str(func) + ": " + str(e)
            print(errorMessage)
            return Response("Error: " + str(e), 500)

    return wrap
