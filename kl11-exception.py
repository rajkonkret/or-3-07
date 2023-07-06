class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    raise MyException("wystąpił wyjątek")  # rzucenie wyjątku, MyException: wystąpił wyjątek
except MyException:
    print("Wystąpił wyjątek MyException")
except Exception as e:
    print("Bład", e)
# 11:25
