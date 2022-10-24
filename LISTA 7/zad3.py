# Zadanie 3 Lista 7

# Importy
from zad1 import Rocket
import random

def main():

    rockets = create_fleet(5)

    print('\n\n')
    for rocket in rockets:
        print(f'Pozycja rakiety nr {rockets.index(rocket) + 1} : {rocket.get_position()}')

    print('************************************')

    while True:

        index = int(input('Podaj numer statku, który chcesz wybrać (1-5): '))
        xoffset = float(input('Podaj wartość o jaką chcesz przesunąć rakietę wzdłuż osi X: '))
        yoffset = float(input('Podaj wartość o jaką chcesz przesunąć rakietę wzdłuż osi Y: '))

        rockets[index - 1].move(xoffset, yoffset)

        for rocket in rockets:
            print(f'\nPozycja rakiety nr {rockets.index(rocket) + 1} : {rocket.get_position()}')
            for other in rockets[rockets.index(rocket) + 1:]:
                print(f'Odległość rakiety nr {rockets.index(rocket) + 1} do rakiety nr {rockets.index(other) + 1} wynosi: {rocket.get_distance(other)}')
        
        print('*****************************\n')



def create_fleet(size):

    rockets = []
    
    for i in range(size):
        rockets.append(Rocket(random.uniform(-10, 10), random.uniform(-10, 10)))

    return rockets

if __name__ == '__main__':
    main()