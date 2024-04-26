
import math
import pygame

from constants import *


class CelestialBody:
    def __init__(self, x, y, radius, colour, mass, isSun = False, isStar = False, isAsteroid = False, showAltitude = True):
        #relative to sun
        self.x = x
        self.y = y


        self.r = radius
        self.colour = colour
        self.m = mass
        self.FONT = pygame.font.SysFont("bahnschriftsemilight", 14)

        # objects defined at perihelion radius and velocity
      #  self.perihelion = radius
       # self.aphelion = 0 # this will change
        #self.aphelionPoint = (0,0)

        self.orbit = []
        self.isSun = isSun # if it's the sun then it's the perspective frame so the orbit doesn't get drawn,
                         # everything else is moving relative to it

        self.isStar = isStar
        self.isAsteroid = isAsteroid

        self.showAltitude = showAltitude

        self.closeApproach = 1*10**99 # an insanely large number (roughyl 10^83 light years)

        self.d_to_sun = 0

        self.xvel = 0
        self.yvel = 0

    def draw(self, window, scale, planetScale, xoffset, yoffset):
        # positions, set to scale and put relative to the centre of the screen
        x = (self.x + xoffset) * scale + window.width /2
        y = (self.y + yoffset) * scale + window.height /2

        if len(self.orbit) > 2:
            updated_points = []

            if len(self.orbit) > ORBITPATHPOINTS + 2: #must have 2+ points
                self.orbit = self.orbit[int(len(self.orbit)-ORBITPATHPOINTS):] # cut off all except latest 1000

            for point in self.orbit:
                x1, y1 = point
                oldY1 = y1
                x1 = (x1 + xoffset) * scale + window.width / 2
                y1 = (y1 + yoffset) * scale + window.height /2

            #    if oldY1 >= self.aphelion:
             #       self.aphelionPoint = (int(x1), int(y1))
              #      print(self.aphelionPoint)
                

                updated_points.append((x1,y1))

            pygame.draw.lines(window.win, self.colour, False, updated_points, 1)

       # if not self.isSun and self.showAltitude:
        #    distance_text = self.FONT.render(f"{round(self.d_to_sun/1000000, 2)}Mm", 1, (255,255,255))
         #   window.win.blit(distance_text, ((x - distance_text.get_width()/2), (y - distance_text.get_height()/2 - 12) ))

            # draw Ap at Aphelion point
            #Ap_text = self.FONT.render(f"Ap  {round(self.aphelion/1000000, 2)}Mm", 1, (255,255,255))
            #window.win.blit(Ap_text, self.aphelionPoint)
        else: # is star
            text = self.FONT.render("Star", 1, (255,255,255))
            window.win.blit(text, ((x - text.get_width()/2), (y - text.get_height()/2 - 12)))



        if self.isSun or self.isStar:
            pygame.draw.circle(window.win, self.colour, (x, y), 10 * planetScale)#self.r * scale)
        elif self.isAsteroid:
            pygame.draw.circle(window.win, self.colour, (x,y), 2 * planetScale)
        else:
            pygame.draw.circle(window.win, self.colour, (x, y), 6 * planetScale)#self.r * scale)

    def findForce(self, other):
        other_x, other_y = other.x, other.y
        #distance
        r_x = other_x - self.x
        r_y = other_y - self.y

        r = math.sqrt(r_x**2 + r_y**2)

        if other.isSun:
            self.d_to_sun = r
                

        
        force = G * self.m * other.m / r**2

        theta = math.atan2(r_y, r_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force 
        return force_x, force_y

    def move(self, bodies):
        if not SUN_STATIONARY or not self.isSun:
            totalf_x, totalf_y = 0,0
            for body in bodies:
                if body != self: # don't want to find gravitational force with itself
                    f_x, f_y= self.findForce(body)
                    totalf_x += f_x
                    totalf_y += f_y


            self.xvel += totalf_x / self.m * TIMESTEP
            self.yvel += totalf_y / self.m * TIMESTEP

            self.x += self.xvel * TIMESTEP
            self.y += self.yvel * TIMESTEP
            
            self.orbit.append((self.x, self.y))

    def closestApproach(self, other):
        d = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        if d < self.closeApproach:
            self.closeApproach = d

        return self.closeApproach

                 
