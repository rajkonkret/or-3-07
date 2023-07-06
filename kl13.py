class MyBaseException(Exception):
    """
    Bazowy wyjątek dla naszych wyjątków
    """

    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

    def print_error(self):
        print(f"Error: {self.args[0]}, Error Code: {self.error_code}")


class NetworkException(MyBaseException):
    """
    Wyjątek dla problemów sieciowych
    """

    def retry(self):
        print("Retrying network operation...")


class DatabaseException(MyBaseException):
    """
    Wyjątek do problemów z bazą danych
    """

    def rollback(self):
        print("Rolling back database transaction...")


try:
    raise NetworkException("Network problem occured", 101)
except NetworkException as e:
    e.print_error()
    e.retry()

try:
    raise DatabaseException("Database problem", 56)
except DatabaseException as e:
    e.print_error()
    e.rollback()
#
# Error: Network problem occured, Error Code: 101
# Retrying network operation...
# Error: Database problem, Error Code: 56
# Rolling back database transaction...