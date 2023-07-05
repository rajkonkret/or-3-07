# funkcja kantor, w niej beda dwie funkcje jedna usd, druga eur

def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota):
        print(f"Wymieniam dolary {kwota} dol = {kwota * 4.1} zł")

    def eur(kwota):
        print(f"Wymieniam euro {kwota} eur = {kwota * 4.42} zł")

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_eur = kantor('eur')
print(kantor_eur)  # <function kantor.<locals>.eur at 0x00000250ABB46FC0>
kantor_eur(1000)  # Wymieniam , Wymieniam euro 1000 eur = 4420.0 zł

# dodac mozliwosc przekazania kwoty do wymiany
# ładnie wypisac wymieniam dolary 100 dolarów = 406 zł
