def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper

    return decorator


@repeat(5)
def greet(name):
    return f"Hello {name}"


print(greet("Radek"))  # ['Hello Radek', 'Hello Radek', 'Hello Radek', 'Hello Radek', 'Hello Radek']

greeetings = greet("Tomek")
for g in greeetings:
    print(g)  # Hello Tomek
