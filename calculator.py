from fompy.materials import Si
from fompy.units import *
from fompy.models import *
from fompy.constants import *

class Silicon_n_type:
    def __init__(self, conc, energy) -> None:
        self.si = DopedSemiconductor(Si, 0, 0, conc, Si.Eg - from_unit(energy, "eV"))
        self.T = 300

    def get_fermi_level(self, temperature=300):
        return self.si.fermi_level(temperature)
        
    def get_params(self, temperature=300):
        fermi_eneregy = self.si.fermi_level(temperature)
        electrons_conc = self.si.n_concentration(fermi_eneregy, temperature)
        return to_unit(fermi_eneregy, "eV"), electrons_conc

    def get_Eg(self):
        return to_unit(Si.Eg, "eV")

    def get_energy_diff(self):
        return to_unit(self.si.Ed, "eV")
