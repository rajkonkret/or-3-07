# funkcja zagnieżdzona
def fun1():
    print("To jest  fun1")

    # deklaracja funkcji fun2
    def fun2():
        print("To jest fun2")

    return fun2  # bez nawiasow, tylko zwracamy adres funkcji a nie wykonujemy ją


xFun = fun1()  # To jest  fun1
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000020519126F20>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2


