import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time} sec")
        return result

    return wrapper


@measure_time
def my_function():
    # pass  # Czas wykonania funkcji my_function: 0.0 sec
    # print(2024 ** 1024)  # Czas wykonania funkcji my_function: 0.0010492801666259766 sec
    time.sleep(2)  # Czas wykonania funkcji my_function: 2.000582695007324 sec - wstrzymanie działania programu na 2s


my_function()
