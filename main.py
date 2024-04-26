import random
import pygame
import math

from planet import CelestialBody
from constants import *
from window import Window

class PlanetSimulator:
    def __init__(self):
        self.window = Window(1000, 820, "Solar System Simulator")
        self.glob = Globals()

    def runSim(self):
        run = True
        clock = pygame.time.Clock()

        objects = []
        #init planets and their orbital linear velocities
        earthRad = 100000000000*6371400 * self.glob.scale
        #ratios:
        #Rm=1/3Re
        #Rv=0.949Re
        #Rma=0.53Re
        #Rj = 10.97Re
        #Rs = 9.14Re
        #Ru = 3.98Re
        #Rn = 3.86Re
        #Rp = 0.187Re

        sun = CelestialBody(0,0, int(109.2*earthRad), (255,255,0),M_SUN,True)
        #sun.xvel = 5000
        #sun.yvel = 2000
        objects.append(sun)

        """
            asteroid belt, random dots with varying velocities within a certain range from the sun
        """

        ##ALL ORBIT RADIUS AND VELOCITIES ARE AT PERIHELION, TAKEN FROM NSSDC NASA FACT SHEETS

        merc = CelestialBody(46 * 10**9, 0, int(earthRad/3), (100,100,100), M_MERC)
        merc.yvel = -58970
        objects.append(merc)
        
        venus = CelestialBody(0, -(107.48* 10**9), int(0.949*earthRad), (163, 104, 2), M_VENUS)
        venus.xvel = -35260
        objects.append(venus)

        earth = CelestialBody(-(147.095 * 10**9), 0, earthRad, (0,255,255), M_EARTH)
        earth.yvel = 30290
        objects.append(earth)


        mars = CelestialBody(0, 206.650 * 10**9, int(0.53*earthRad), (190,71,43), M_MARS)
        mars.xvel = 26500
        objects.append(mars)

        ###ASTEROID BELT
        for i in range (0):
            mass = random.uniform(10**12, 10**14)
            orbitradius = random.uniform(2.2*AU, 3.2*AU)
            velocity = random.uniform(17000,19000)
            #roughly 100m - 200km in radius
            radius = random.uniform(0.000016*earthRad, 0.0314*earthRad)
            positionChance = random.randint(1,4)
            if positionChance == 1:
                asteroid = CelestialBody(orbitradius, 0, radius, (50, 50,60), mass, False, False, True, False)
                asteroid.yvel = -velocity
                objects.append(asteroid)
            if positionChance == 2:
                asteroid = CelestialBody(-orbitradius, 0, radius,  (50, 50,60), mass, False, False, True, False)
                asteroid.yvel = velocity
                objects.append(asteroid)
            elif positionChance == 3:
                asteroid = CelestialBody(0, orbitradius, radius,   (50, 50,60), mass, False, False, True, False)
                asteroid.xvel = velocity
                objects.append(asteroid)
            elif positionChance == 4:
                asteroid = CelestialBody(0, -orbitradius, radius,   (50, 50,60), mass, False, False, True, False)
                asteroid.xvel = -velocity
                objects.append(asteroid)


        jup = CelestialBody(740.595 * 10**9, 0, int(10.97*earthRad), (255,180,0), M_JUP)
        jup.yvel = -13720
        objects.append(jup)

        sat = CelestialBody(0, -(1357.554 * 10**9), int(9.14*earthRad), (255,255,100), M_SAT)
        sat.xvel = -10140
        objects.append(sat)

        ura = CelestialBody(-(2732.696 * 10**9), 0, int(10.97*earthRad), (160,160,255), M_URA)
        ura.yvel = 7130
        objects.append(ura)

        nep = CelestialBody(0, 4471.050 * 10**9, int(10.97*earthRad), (50,100,255), M_NEP)
        nep.xvel = 5470
        objects.append(nep)

        pluto = CelestialBody(4434.987 * 10**9, 0, int(0.187*earthRad), (255, 225, 225), M_PLU)
        pluto.yvel = -6100
        objects.append(pluto)
        
        sedna = CelestialBody(-(937*AU), 0, int(0.09*earthRad), (255,150,150),  M_SED)
        sedna.yvel = 387.14
        objects.append(sedna)


        ##other stars SYSTEM
        #-(4.246*63241.1*AU)
        #star = CelestialBody(5*AU, 0, 5, (255,100,0), 5*M_SUN, False, True)
        #star.yvel = -30000 * 1.5
        #objects.append(star)
       # alphacenA = CelestialBody(-(4.246*63241.1*AU + 12950*AU), 0, 5, (255,255,0), M_ALPHACENA, False, True)
       # objects.append(alphacenA)


        rocket_pos = None

        xoffset = 0
        yoffset = 0

        while run:
            clock.tick(FPS)
            self.window.clear()
           
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEWHEEL:
                    scalar = (event.y + 2)/2 #brings it to range 0.5-1.5 instead of -1-1
                        
                    self.glob.scale = self.glob.scale * scalar
                    self.glob.planetScale = self.glob.planetScale * scalar
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        xoffset += 100 / self.glob.scale
                    if event.key == pygame.K_RIGHT:
                        xoffset -= 100 / self.glob.scale
                    if event.key == pygame.K_UP:
                        yoffset += 100 / self.glob.scale
                    if event.key == pygame.K_DOWN:
                        yoffset -= 100 / self.glob.scale
                #if event.type == pygame.MOUSEBUTTONDOWN:
                #    if rocket_pos:
                #        #move in direction of mouse
                #        r_x, r_y = rocket_pos
                #        m_x, m_y = mouse_pos

                #        dx = m_x - r_x
                #        dy = m_y - r_y

                #        vx = 0.03*dx
                #        vy = 0.03*dy
                #        
                #        rocket = Rocket(r_x, r_y, vx,vy,40000, (90, 90, 100), self.window.win)
                #        objects.append(rocket)
                #        rocket_pos = None
                #    else:
                #        rocket_pos = mouse_pos

            self.window.clear()
            for body in objects:
                body.move(objects)
                
                body.draw(self.window, self.glob.scale, self.glob.planetScale, xoffset, yoffset)
            
            #chance = random.randint(1, FPS)
            #pnca = pluto.closestApproach(nep)/AU
          #  if chance == FPS // 2: # one in fps chance
           #     print("Pluto/Neptune closest approach: " + str(round(pnca, 4)) + "AU")


            pygame.display.update()
        
        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    ps = PlanetSimulator()
    ps.runSim()
