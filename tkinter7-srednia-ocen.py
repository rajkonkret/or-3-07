import tkinter as tk


class GradeCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Grade Calculator")

        self.student_var = tk.StringVar(master)
        self.student_var.set("Uczeń 1")
        self.student_dropdown = tk.OptionMenu(master, self.student_var,
                                              "Uczeń 1", "Uczeń 2", "Uczeń 3")

        self.student_dropdown.pack()

        self.grade_entry = tk.Entry(master, width=10)
        self.grade_entry.pack()

        self.add_button = tk.Button(master, text="Dodaj ocenę", command=self.add_grade)
        self.add_button.pack()

        self.grades_label = tk.Label(master, text="Dotychczasowe oceny")
        self.grades_label.pack()

        self.average_label = tk.Label(master, text="Średnia: ")
        self.average_label.pack()

        self.grades_dict = {"Uczeń 1": [], "Uczeń 2": [], "Uczeń 3": []}

    def add_grade(self):
        grade = self.grade_entry.get()
        grade = float(grade)
        student = self.student_var.get()

        self.grades_dict[student].append(grade)
        self.grade_entry.delete(0, tk.END)  # czyszczenie okienka Entry od znaku 0 do ostatniego

        self.grades_label.config(text="Dotychczsowe oceny: " + str(self.grades_dict[student]))

        # sum - sumuje wartosci elemntów , len - zwraca długosc słownika
        average = sum(self.grades_dict[student]) / len(self.grades_dict[student])
        self.average_label.config(text="Średnia: " + str(average))


root = tk.Tk()
calculator_app = GradeCalculator(root)
root.mainloop()
