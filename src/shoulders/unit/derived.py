from shoulders.dimension.base import *
from shoulders.dimension.derived import *

from .unit import Unit

# === The 22¹ SI units with special name and symbols ===
# ¹21 actually, Celsius temperature is missing because it has to be convert from kelvin

RADIAN = Unit('rad', PLANE_ANGLE, {'rad': 1})
rad = RADIAN

STERADIAN = Unit('sr', SOLID_ANGLE, {'sr': 1})
sr = STERADIAN

HERTZ = Unit('Hz', FREQUENCY, {'Hz': 1})
Hz = HERTZ

NEWTON = Unit('N', FORCE, {'N': 1})
N = NEWTON

# pressure & stress
PASCAL = Unit('Pa', FORCE / LENGTH**2, {'Pa': 1})
Pa = PASCAL

# energy, work & amount of heat
JOULE = Unit('J', FORCE * LENGTH, {'J': 1})
J = JOULE

WATT = Unit('W', POWER, {'W': 1})
W = WATT

COULOMB = Unit('C', ELECTRIC_CHARGE, {'C': 1})
C = COULOMB

VOLT = Unit('V', ELECTRIC_POTENTIAL_DIFFERENCE, {'V': 1})
V = VOLT

OHM = Unit('Ω', ELECTRICAL_RESISTANCE, {'Ω': 1})
Ω = OHM

SIEMENS = Unit('S', ELECTRICAL_CONDUCTANCE, {'S': 1})
S = SIEMENS

FARAD = Unit('F', CAPACITANCE, {'F': 1})
F = FARAD

WEBER = Unit('Wb', MAGNETIC_FLUX, {'Wb': 1})
Wb = WEBER

HENRY = Unit('H', INDUCTANCE, {'H': 1})
H = HENRY

TESLA = Unit('T', MAGNETIC_FLUX_DENSITY, {'T': 1})
T = TESLA

LUMEN = Unit('lm', LUMINOUS_FLUX, {'lm': 1})
lm = LUMEN

LUX = Unit('lx', ILLUMINANCE, {'lx': 1})
lx = LUX

BECQUEREL = Unit('Bq', RADIONUCLIDE_ACTIVITY, {'Bq': 1})
Bq = BECQUEREL

# aborbed dose & kerma
GRAY = Unit('Gy', ENERGY / MASS, {'Gy': 1})
Gy = GRAY

SIEVERT = Unit('Sv', DOSE_EQUIVALENT, {'Sv': 1})
Sv = SIEVERT

KATAL = Unit('kat', CATALYTIC_ACTIVITY, {'kat': 1})
kat = KATAL

# TODO: Make a way that a unit can link with two or more quantities
# TODO: Make all the derived units