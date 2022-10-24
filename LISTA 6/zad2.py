# Zadanie 2 Lista 6

# Importy
import math

# Funkcja wykrywająca kolizję pomiędzy dwoma dyskami
def collision(first_disc, second_disc):

    first_center, second_center = first_disc[0], second_disc[0]
    first_radius, second_radius = first_disc[1], second_disc[1]

    distance = math.sqrt((first_center[0] - second_center[0])**2 + (first_center[1] - second_center[1])**2)

    if first_radius + second_radius > distance:
        return True
    return False

disc1 = [[1, 0], 1]
disc2 = [[1, 2], 1]

print(collision(disc1, disc2))