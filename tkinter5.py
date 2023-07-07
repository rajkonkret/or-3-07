import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_711 = tk.Button(root)
        GButton_711["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_711["font"] = ft
        GButton_711["fg"] = "#000000"
        GButton_711["justify"] = "center"
        GButton_711["text"] = "Button"
        GButton_711.place(x=70, y=70, width=70, height=25)
        GButton_711["command"] = self.GButton_711_command

        GLabel_838 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_838["font"] = ft
        GLabel_838["fg"] = "#333333"
        GLabel_838["justify"] = "center"
        GLabel_838["text"] = "label"
        GLabel_838.place(x=210, y=40, width=70, height=25)

        GCheckBox_979 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_979["font"] = ft
        GCheckBox_979["fg"] = "#333333"
        GCheckBox_979["justify"] = "center"
        GCheckBox_979["text"] = "CheckBox"
        GCheckBox_979.place(x=380, y=70, width=70, height=25)
        GCheckBox_979["offvalue"] = "0"
        GCheckBox_979["onvalue"] = "1"
        GCheckBox_979["command"] = self.GCheckBox_979_command

        GRadio_478 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_478["font"] = ft
        GRadio_478["fg"] = "#333333"
        GRadio_478["justify"] = "center"
        GRadio_478["text"] = "RadioButton"
        GRadio_478.place(x=70, y=200, width=85, height=25)
        GRadio_478["command"] = self.GRadio_478_command

        GLineEdit_729 = tk.Entry(root)
        GLineEdit_729["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_729["font"] = ft
        GLineEdit_729["fg"] = "#333333"
        GLineEdit_729["justify"] = "center"
        GLineEdit_729["text"] = "Entry"
        GLineEdit_729.place(x=270, y=170, width=70, height=25)

        GListBox_680 = tk.Listbox(root)
        GListBox_680["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_680["font"] = ft
        GListBox_680["fg"] = "#333333"
        GListBox_680["justify"] = "center"
        GListBox_680.place(x=90, y=290, width=80, height=25)
        GListBox_680["exportselection"] = "1"
        GListBox_680["listvariable"] = "e"

        GMessage_318 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_318["font"] = ft
        GMessage_318["fg"] = "#333333"
        GMessage_318["justify"] = "center"
        GMessage_318["text"] = "moj komunikat"
        GMessage_318.place(x=280, y=270, width=158, height=30)

    def GButton_711_command(self):
        print("command")

    def GCheckBox_979_command(self):
        print("command")

    def GRadio_478_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
