# Zadanie 4 Lista 7

'''

RAKIETĄ PORUSZAMY SIĘ STRZAŁKAMI!!!!

'''

import math
import sys
import pygame

# Stałe określające rozmiar okna
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Stałe określające rozmiar rakiety
ROCKET_WIDTH = ROCKET_HEIGHT = 32

class Rocket:
    
    # Metoda inicjalizująca obiekt klasy Rocket z domyślnym położeniem (0, 0) oraz domyślną prędkością (0, 0)
    def __init__(self, x=0, y=0, xspeed=0, yspeed=0) -> None:
        self.position = [x, y]
        self.xspeed = xspeed
        self.yspeed = yspeed
    
    # Metoda aktualizująca położenie rakiety
    def move(self):
        self.position[0] += self.xspeed
        self.position[1] += self.yspeed

    # Metoda nadająca przyspieszenie rakiecie
    def accelerate(self, x, y):
        self.xspeed = self.xspeed + x if self.xspeed <= 1 else self.xspeed
        self.yspeed = self.yspeed + y if self.yspeed <= 1 else self.yspeed

    # Metoda symulująca opór 
    def deaccelerate(self):
        self.xspeed *= 0.9
        self.yspeed *= 0.9

    # Metoda zwracająca pozycję obiektu klasy Rocket
    def get_position(self):
        return self.position

    # Metoda zwracająca pseudonim obiektu klasy Rocket
    def get_name(self):
        return self.name

    # Metoda zwracająca odległość pomiędzy dwoma obiektami klasy Rocket
    def get_distance(self, other):
        return math.sqrt((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2)

    # Metoda sprawdzająca czy rakieta jest w obszarze ekranu 
    def check_boundaries(self):

        if self.position[0] <= 0 or self.position[0] + ROCKET_WIDTH >= SCREEN_WIDTH:
            self.xspeed = -self.xspeed
        if self.position[1] <= 0 or self.position[1] + ROCKET_HEIGHT >= SCREEN_HEIGHT:
            self.yspeed = -self.yspeed

    # Metoda pozwalająca na poruszanie rakietą po ekranie
    def play(self):

        # Inicjalizacja biblioteki pygame
        pygame.init()

        # Utworzenie okienka windowsowego
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Rakieta")
        icon = pygame.image.load('rocket.png')
        pygame.display.set_icon(icon)

        # Utworzenie rakiety na ekranie
        rocket_image = pygame.image.load('rocket.png')

        framecount = 0

        # Główna pętla
        while True:

            
            for event in pygame.event.get():
                
                # Zakończenie programu w przypadku zamknięcia okienka
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        self.accelerate(0, -0.1)

                    elif event.key == pygame.K_DOWN:
                        self.accelerate(0, 0.1)

                    elif event.key == pygame.K_RIGHT:
                        self.accelerate(0.1, 0)

                    elif event.key == pygame.K_LEFT:
                        self.accelerate(-0.1, 0)
            
            # Przesuwanie rakiety po ekranie
            self.move()
            self.check_boundaries()

            # Wytracanie prędkości przez rakietę
            if framecount % 100 == 0:
                self.deaccelerate()
            
            screen.fill((0, 0, 0))
            screen.blit(rocket_image, self.position)
            pygame.display.update()

            framecount += 1



def main():

    rocket = Rocket(600, 300)
    rocket.play()

main()
    