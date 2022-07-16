class Logger:
    def log(self, location, msg):
        print(self.__class__.__name__.upper() + ": " + location + " -> " + msg)