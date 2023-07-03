tekst = "Witaj świecie"
print(tekst)  # Witaj świecie

tekst2 = tekst.upper()  # """ Return a copy of the string converted to uppercase. """
print(tekst)
print(tekst2)  # WITAJ ŚWIECIE
# teksty sa niemutowalne
print(tekst.lower())  # witaj świecie
print(tekst)  # Witaj świecie

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst)  # Witaj świecie

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie
# indeksy startuja od 0
print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # 1

print(len(tekst))  # długosc tekstu = 13

imie = "Radek"
tekst_format = f"\tMam na imię {imie}\n i lubie Pythona \b"
print(tekst_format)
# "	Mam na imię Radek
#  i lubie Pythona
# "
# \t - tabulator
# \n = znak nowej linii
# \b - backspace - czyli usuwa znak bezpośrednio przed nim
# 11:25

starszy = "Witaj %s"
# %s - oznacz wstaw w to miejsce string
print(starszy % imie)  # Witaj Radek

print("""
    Tekst
wielolinijkowy""")

# "    Tekst
# wielolinijkowy"

print("Witaj {}".format(imie))  # Witaj Radek
