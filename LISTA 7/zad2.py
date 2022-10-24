# Zadanie 2 Lista 7

# Importy
from zad1 import Rocket

def main():

    rocket = Rocket(10, 10)

    for x, y in zip(range(10), range(10)):
        rocket.move(x + 1, -y - 1)
        print(f'Pozycja statku po przesunięciu o x:{x + 1}, y:{-y - 1} :', rocket.get_position())

if __name__ == '__main__':
    main()
