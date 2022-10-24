# Zadanie 4 Lista 6
import math

def collision(first_disc, second_disc):

    '''
    Zwraca True jeżeli dwa dyski są w kolizji, False w przeciwnym wypadku

    Argumenty:

    first_disc, second_disc --- dwa dyski do sprawdzenia kolizji

    '''

    first_center, second_center = first_disc[0], second_disc[0]
    first_radius, second_radius = first_disc[1], second_disc[1]

    distance = math.sqrt((first_center[0] - second_center[0])**2 + (first_center[1] - second_center[1])**2)

    if first_radius + second_radius > distance:
        return True
    return False


def move_disc(disc, vector):
    
    '''
    Zwraca nowy dysk, przesunięty o zadany wektor

    Argumenty:

    disc    --- dysk do przesunięcia
    vector  --- wektor, o który dysk ma być przesunięty

    '''

    new_center = (disc[0][0] + vector[0], disc[0][1] + vector[1])

    return [new_center, disc[1]]
