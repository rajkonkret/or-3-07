import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()

fig = Figure(figsize=(5, 4), dpi=100)

ax = fig.add_subplot(111)

t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2 * np.pi * t)

ax.plot(t, s)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()
