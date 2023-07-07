import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Sklep:
    def __init__(self, master):
        self.master = master
        self.master.title("Gra Sklep")

        self.produkty = {
            "Chleb": 3,
            "Mleko": 2,
            "Jaja": 5
        }

        self.zakupy = {}  # pusty słownik

        # labelka tytułowa
        ttk.Label(self.master, text="Produkty w sklepie").grid(column=0, row=0, pady=5)

        # wypisanie w poszczególnych wierszach produktow i cen produktów
        for index, product in enumerate(self.produkty):
            ttk.Label(self.master, text=f"{product}: {self.produkty[product]} zł").grid(
                column=0, row=index + 1, pady=5, padx=5
            )

            self.zakupy[product] = tk.IntVar()
            ttk.Entry(self.master, textvariable=self.zakupy[product]).grid(
                column=1, row=index + 1, pady=5, padx=5
            )
        ttk.Button(self.master, text="Złóż zamówienie", command=self.zloz_zamowienie).grid(
            column=0, row=len(self.produkty) + 1, padx=5, pady=5, columnspan=2
        )

    def zloz_zamowienie(self):
        suma = 0
        for produkt in self.produkty:
            ilosc = self.zakupy[produkt].get()
            cena = self.produkty[produkt] * ilosc
            suma += cena

        tk.messagebox.showinfo("Podsumowanie zamówienia", f"Koszt: {suma} zł")


okno = tk.Tk()
sklep = Sklep(okno)
okno.mainloop()
