import pandas as pd
# pip install pandas

data = pd.read_csv('records.csv')
print(data)
#     name branch  year  cgpa
# 0  Tomek    COE     2   9.1
# 1  Radek    COE     2   9.0
# 2   Asia    COE     2   9.1
# 3  Radek    COT     2   9.1
# 4  Zenek    COE     3   9.2
# 5  Radek    CtI     2   9.1
# 6  radek    coe     3   9.0

print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['Tomek' 'COE' 2 9.1]
#  ['Radek' 'COE' 2 9.0]
#  ['Asia' 'COE' 2 9.1]
#  ['Radek' 'COT' 2 9.1]
#  ['Zenek' 'COE' 3 9.2]
#  ['Radek' 'CtI' 2 9.1]
#  ['radek' 'coe' 3 9.0]]
print(data.values[0])  # ['Tomek' 'COE' 2 9.1]
print(type(data.values[0]))  # <class 'numpy.ndarray'>
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  Tomek    COE     2   9.1
# 1  Radek    COE     2   9.0
# 2   Asia    COE     2   9.1
# 3  Radek    COT     2   9.1
# 4  Zenek    COE     3   9.2
# 5  Radek    CtI     2   9.1
# 6  radek    coe     3   9.0>