from fompy.materials import Si
from fompy.units import *
from fompy.models import *
from fompy.constants import *

class Silicon_n_type:
    def __init__(self) -> None:
        self.si = DopedSemiconductor(Si,0, 0, 1e15, from_unit(1.12, "eV"))
        self.T = 300
    def set_donor_energy(self, donor_energy=1.12):
        self.si.Ed = from_unit(donor_energy, "eV")

    def get_fermi_level(self, temperature=300):
        return self.si.fermi_level(temperature)

    def set_donor_concenctration(self, donor_concentration=1e15):
        self.si.Nd = donor_concentration
