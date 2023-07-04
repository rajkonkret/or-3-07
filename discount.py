from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-07-04
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2023-07-04 09:51:43.426670
print(type(time))  # <class 'datetime.datetime'>

# , days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
# t2 = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
print(tomorrow)

print(time.hour)  # 9
print(today.day)  # 4

formmated_date = datetime.now().strftime("%d/%m/%Y")
print(formmated_date)  # 04/07/2023

formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 09:58

formted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(formted_datetime)  # 2023-07-04 10:00:10

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomorrow, 'price': 50.0},
    {'sku': 3, 'exp_date': today, 'price': 20},
    {'sku': 4, 'exp_date': today, 'price': 120},
    {'sku': 5, 'exp_date': tomorrow, 'price': 30.0},
    {'sku': 6, 'exp_date': today, 'price': 15},
    {'sku': 7, 'exp_date': today, 'price': 145.50},
]
print(products)
# [{'sku': 1, 'exp_date': datetime.date(2023, 7, 4), 'price': 100.0},
#  {'sku': 2, 'exp_date': datetime.date(2023, 7, 5), 'price': 50.0},
#  {'sku': 3, 'exp_date': datetime.date(2023, 7, 4), 'price': 20}]

for product in products:
    if product['exp_date'] != today:
        continue  # wróci na początek pętli

    product['price'] *= 0.8  # price = price * 0.8
    print(f"""
    Price for sku = {product['sku']}
    is now {product['price']}""")
