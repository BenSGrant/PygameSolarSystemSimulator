
## CONSTANTS
# Physical constants
G = 6.67428 * 10 **(-11)     # Gravitational constant
AU = 149597870700         # /m

# Masses /kg
M_SUN = 1.98892 * 10**(30)
M_MERC = 3.285 * 10**(23)
M_VENUS = 4.867  * 10**(24)
M_EARTH = 5.9742 * 10**(24)
M_MOON = 7.34767309 * 10**(22)
M_MARS = 6.39 * 10**(23)
M_JUP = 1.898 * 10**(27)
M_SAT = 5.683 * 10**(26)
M_URA = 8.681 * 10**(25)
M_NEP = 1.024 * 10**(26)
M_PLU = 1.309 * 10**(22)
M_SED = 3.05 * 10**21 # mean of the 2 limitng values of the range given in a google search

M_PROXCEN = 0.1221 * M_SUN
M_ALPHACENA = 1.0788 * M_SUN
# radii /m
R_SUN = 696340000
R_EARTH = 6371000


FPS = 60

TIMESTEP = 3600*24*7*13/FPS#(3600*24*7*52*20)/FPS # how many simulation seconds pass per second

SUN_STATIONARY = False

ORBITPATHPOINTS = 1000000000 // TIMESTEP

class Globals:
    def __init__(self):
        self.scale = 75/AU # 1AU roughly = 100px when scale = 250/AU
        self.planetScale = 1

    def mulScale(self,a):
        self.scale = self.scale * a
