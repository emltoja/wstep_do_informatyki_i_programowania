# Zadanie 1 Lista 7

# Importy
from math import sqrt

class Rocket:


    # Metoda inicjalizująca obiekt klasy Rocket z domyślnym położeniem (0, 0)
    def __init__(self, x=0, y=0) -> None:
        self.position = [x, y]

    # Metoda przesuwająca obiekt klasy Rocket o x wzdłuż osi X i o y wzdłuż osi Y
    def move(self, x, y):
        self.position[0] += x
        self.position[1] += y

    # Metoda zwracająca pozycję obiektu klasy Rocket
    def get_position(self):
        return self.position

    # Metoda zwracająca odległość pomiędzy dwoma obiektami klasy Rocket
    def get_distance(self, other):
        return sqrt((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2)
        
    