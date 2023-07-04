import pandas as pd

excel_data = pd.read_excel("sales.xlsx")
# data = pd.DataFrame(excel_data,columns=["Sales Date"])
data = pd.DataFrame(excel_data)

print("The content is:\n", data)
# The content is:
#    Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000

print(data.columns)
print(data.items)
print(data.values)
# Index(['Sales Date'], dtype='object')

# <bound method DataFrame.items of   Sales Date
# 0 2018-05-12
# 1 2019-12-06
# 2 2020-08-09
# 3 2021-04-07>
# [['2018-05-12T00:00:00.000000000']
#  ['2019-12-06T00:00:00.000000000']
#  ['2020-08-09T00:00:00.000000000']
#  ['2021-04-07T00:00:00.000000000']]