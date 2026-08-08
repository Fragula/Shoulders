from shoulders.dimension.base import *
from shoulders.dimension.derived import *

from .unit import Unit

# === The 22¹ SI units with special name and symbols ===
# ¹21 actually, Celsius temperature is missing because it has to be convert from kelvin

RADIAN = Unit('radian', 'rad', PLANE_ANGLE)
STERADIAN = Unit('steradian', 'sr', SOLID_ANGLE)
HERTZ = Unit('hertz', 'Hz', FREQUENCY)
NEWTON = Unit('newton', 'N', FORCE)
PASCAL = Unit('pascal', 'Pa', FORCE / LENGTH**2)  # energy, work & amount of heat
JOULE = Unit('joule', 'J', FORCE * LENGTH)  # pressure & stress
WATT = Unit('watt', 'W', POWER)
COULOMB = Unit('coulomb', 'C', ELECTRIC_CHARGE)
VOLT = Unit('volt', 'V', ELECTRIC_POTENTIAL_DIFFERENCE)
OHM = Unit('ohm', 'Ω', ELECTRICAL_RESISTANCE)
SIEMENS = Unit('siemens', 'S', ELECTRICAL_CONDUCTANCE)
FARAD = Unit('farad', 'F', CAPACITANCE)
WEBER = Unit('weber', 'Wb', MAGNETIC_FLUX)
HENRY = Unit('henry', 'H', INDUCTANCE)
TESLA = Unit('tesla', 'T', MAGNETIC_FLUX_DENSITY)
LUMEN = Unit('lumen', 'lm', LUMINOUS_FLUX)
LUX = Unit('lux', 'lx', ILLUMINANCE)
BECQUEREL = Unit('becquerel', 'Bq', RADIONUCLIDE_ACTIVITY)
GRAY = Unit('gray', 'Gy', ENERGY / MASS)  # aborbed dose & kerma
SIEVERT = Unit('sievert', 'Sv', DOSE_EQUIVALENT)
KATAL = Unit('katal', 'kat', CATALYTIC_ACTIVITY)

# TODO: Make a way that a unit can link with two or more quantities