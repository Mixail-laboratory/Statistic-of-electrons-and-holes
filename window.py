from ui import *
from PyQt5 import QtWidgets
import numpy as np
import pyqtgraph as pg
from decimal import Decimal

from calculator import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Application()
        self.ui.setupUi(self)
        self.silicon = Silicon_n_type()
        self.E_g = 1.12 
        # 1e+15 : 1e+22 per sm
        self.N_d0 = 1e+15
    
        self.x1 = np.linspace(-5, 5, 200)
        self.plot = self.ui.plot1.plot(pen=pg.mkPen(color='g', width=2))
        self.plot2 = self.ui.plot2.plot(pen=pg.mkPen(color='g', width=2))
        self.line = self.ui.plot2.plot([10, 1200], [1.12, 1.12], pen=pg.mkPen(color='r', width=2))
        self.E_dChanged(0)
        self.N_d0Changed(1500)
        self.plotData()
        self.plotData()
        self.plotData2_n()
        self.plotData2_n()
        self.ui.Ed_silder.valueChanged.connect(self.E_dChanged)
        self.ui.Nd0_slider.valueChanged.connect(self.N_d0Changed)

        self.sols = []
        self.T_range = []

    def E_dChanged(self, val):
        valf = float(val) / 100
        self.E_d = valf 
        self.ui.Ed_lineEdit.clear()
        self.ui.Ed_lineEdit.insert(str(valf) + ', eV')
        self.plotData2_n()
        self.plotData()

    def N_d0Changed(self, val):
        valf = val / 100
        valf = 10 ** valf
        self.N_d0 = valf
        self.ui.Nd0_lineEdit.clear()
        self.ui.Nd0_lineEdit.insert(f"{Decimal(valf):.2E}")
        self.plotData2_n()
        self.plotData()

    def plotData(self):
        pass
    def plotData2(self):
        T1 = np.linspace(0, 400, 300)
        pass
    def plotData2_n(self):
        pass