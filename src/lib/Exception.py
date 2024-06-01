class CustomError(Exception):
    
    def __init__(self, status_code, message="A custom error occurred"):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)
