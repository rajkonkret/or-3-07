# argumenty słownikowe
def connect(**opcje):
    print(opcje)
    print(type(opcje))  # <class 'dict'>
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)
    print(type(connect_param))  # {'host': '127.0.0.7', 'port': '8080'}
    connect_param['pwd'] = opcje
    print(connect_param)
    # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'klucz': 'wartosc'}}
    connect_param.update({'pwd2': opcje})
    print(connect_param)
    # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'klucz': 'wartosc'}, 'pwd2': {'klucz': 'wartosc'}}
    print(connect_param['pwd']['klucz'])  # wartosc


def connect2(*opcje):
    print(opcje)  # ({'name': 'Radek'},)


connect2({'name': "Radek"})

# connect(1)  # TypeError: connect() takes 0 positional arguments but 1 was given
# connect(1, 2, 3)
# 1,2,3,4,5,6,7 - lista, krotka, set
# klucz=warotsc
connect(klucz="wartosc")  # {'klucz': 'wartosc'}
connect(klucz="wartosc", root="/", port="9090")  # {'klucz': 'wartosc'}
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'klucz': 'wartosc', 'root': '/', 'port': '9090'},
#  'pwd2': {'klucz': 'wartosc', 'root': '/', 'port': '9090'}}
connect(klucz="wartosc", a=8)  # {'klucz': 'wartosc', 'a': 8}
