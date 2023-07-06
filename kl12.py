class CustomException(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code

    def print_error(self):
        print(f"Error: {self.args[0]}, Status Code: {self.status_code} ")


try:
    raise CustomException("Error: Coś poszło nie tak, Status Code: 500", 500)
except CustomException as e:
    e.print_error()  # Error: Coś poszło ne tak, Status Code: 500
