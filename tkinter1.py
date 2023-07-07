# tkinter - biblioteka do aplikacji okienkowych
import tkinter


# definicja klasy
class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()  # tworzenie okienka

        self.label1 = tkinter.Label(self.main_window, text="Witaj Świecie")
        self.label2 = tkinter.Label(self.main_window, text="Program Python")
        self.label3 = tkinter.Label(self.main_window, text="Top")
        self.label4 = tkinter.Label(self.main_window, text="Bottom")

        self.label1.pack(side="left")
        self.label2.pack(side="right")
        self.label3.pack(side="top")
        self.label4.pack(side="bottom")

        tkinter.mainloop()
        # top, bottom, right


my_gui = MyGui()
