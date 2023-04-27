class Logger:

    DEBUG = False
    
    def log(s):
        if Logger.DEBUG:
            print (s)
