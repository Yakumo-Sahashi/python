class ExceptionPersonalizada(Exception):
    
    def __init__(self,mensaje):
        self.message = mensaje