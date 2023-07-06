import pakiet
import pakiet.fun as pk
from pakiet import fun

print(pakiet)
# <module 'pakiet' from 'C:\\Users\\CSComarch\\PycharmProjects\\or-3-07\\pakiet\\__init__.py'>
pk.powitanie()  # Cześć
fun.powitanie()
pakiet.powitanie()
fun.info()
pk.info()
# pakiet.info()  # AttributeError: module 'pakiet' has no attribute 'info'
