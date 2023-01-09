from tkinter import *
import matplotlib as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

from fompy import units

import numpy as np
from calculator import *
from calculator import Silicon_n_type
temperatures = np.arange(10, 1200, 50)

fermi_levels = []

electrons_concentration = []



def show_values(dummy=0):
    fermi_levels.clear()
    electrons_concentration.clear()
    semiconductor = Silicon_n_type(w2.get(), w1.get())
    for temp in temperatures:

        fermi, concentation = semiconductor.get_params(temp)
        fermi_levels.append(fermi)
        electrons_concentration.append(concentation)
    print(to_unit(semiconductor.get_fermi_level(), "eV"))
    axes.clear()
    axes_2.clear()
    axes.plot(temperatures, fermi_levels)
    axes.axhline(y = semiconductor.get_Eg(), color = 'r', linestyle = '-')
    axes.axhline(y = semiconductor.get_energy_diff(), color = 'r', linestyle = 'dotted')
     
    axes.set_ylabel('Fermi level, eV')
    axes.set_xlabel('Temperature, K')

        
    axes_2.plot(temperatures, electrons_concentration)
    axes_2.set_xlabel('Temperature, K')
    axes_2.set_ylabel('Electrons concetration, 1/cm^-3')

    figure_canvas.draw()
    figure_canvas_2.draw()

    



master = Tk()
master.title("Task4")

master.geometry("1200x700")

        # create a figure
figure = Figure(figsize=(5, 2), dpi=100)

figure_2 = Figure(figsize=(5, 2), dpi=100)

        # create FigureCanvasTkAgg object
figure_canvas = FigureCanvasTkAgg(figure, master)

figure_canvas_2 = FigureCanvasTkAgg(figure_2, master)



axes = figure.add_subplot()
axes_2 = figure_2.add_subplot()
        # create the barchart
#axes.plot(temperatures, fermi_levels)
axes.set_ylabel('Fermi level, eV')
axes.set_xlabel('Temperature, K')
axes_2.set_xlabel('Temperature, K')
axes_2.set_ylabel('Electrons concetration, 1/cm^-3')

figure_canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)

figure_canvas_2.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)


w1 = Scale(master, from_=0.1, to=1.12, orient=HORIZONTAL, resolution=0.01, label="Donor energy, eV", command=show_values)
w1.set(0.5)
w1.pack(side=TOP)
w2 = Scale(master, from_=1e+15, to=1e+20, orient=HORIZONTAL, resolution=1e+7, label="Donor concentration", command=show_values)
w2.set(1e+17)
w2.pack(side=TOP)



master.mainloop()