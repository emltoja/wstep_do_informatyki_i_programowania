# Lista 6 Zadanie 5

'''

    Dyski są reprezentowane jako dwuelementowa lista, której
    pierwszym elementem jest kolejna dwuelementowa lista 
    przedstawiająca położenie środka dysku, a drugim liczba 
    zmiennoprzecinkowa reprezentująca promień

    ------------------------------------
    [[x, y], r]
    ------------------------------------

'''

# Importy 
from mojefunkcje import collision, move_disc
import math
import random
import matplotlib.pyplot as plt


# Stałe 
SIZE = 15 # Stała określająca rozmiar planszy
RADIUS = 0.5 # Stała określająca promień dysków


# Funkcja zwracająca odległość pomiędzy dwoma dyskami
def distance(first, second):
    return math.sqrt((first[0][0] - second[0][0])**2 + (first[0][1] - second[0][1])**2)


# Funkcja zwracająca znak podanej wartości (zawraca 1 dla 0)
def sign(x):
    return 1 if x >= 0 else -1


# Funkcja zwracająca True jeżeli dysk znajduje się w planszy, False w przeciwnym razie
def check_boundaries(disc):
    return abs(disc[0][0]) <= SIZE - RADIUS and abs(disc[0][1]) <= SIZE - RADIUS


# Funkcja zwracająca listę o zadanej ilości dysków
def get_discs(number):

    result = []

    for i in range(number):
        
        # Wygenerowanie losowych współrzęcnych w obrębie planszy
        x = random.uniform(-SIZE + RADIUS, SIZE - RADIUS)
        y = random.uniform(-SIZE + RADIUS, SIZE - RADIUS)

        result.append([[x, y], RADIUS])

    return result


# Funkcja zwracająca listę wszystkich kolizji pomiędzy dyskami
# Elementami tej listy są pary uporządkowane, których współrzędnymi
# są indeksy dysków, które są ze sobą w kolizji
def check_collisions(discs):

    result = []

    for disc in discs:
        # Sprawdzanie można zacząć od kolejnego dysku, ponieważ wcześniejsze były już sprawdzane wcześniej
        for another in discs[discs.index(disc) + 1:]:

            if collision(disc, another):
                result.append((discs.index(disc), discs.index(another)))

    return result


# Funkcja zwracająca konfigurację dysków z usuniętymi kolizjami
def spread_discs(discs):

    result = discs.copy()
    collisions = check_collisions(result)

    # Dyski rozsuwamy aż do usunięcia ostatniej z kolizji
    while len(collisions) != 0:

        for pair in collisions:

            first_disc = result[pair[0]]
            second_disc = result[pair[1]]

            # Wartości opisujące wektor potrzebny do rozsunięcia obu dysków
            excess_length = first_disc[1] + second_disc[1] - distance(first_disc, second_disc)
            r = excess_length / 2
            angle = math.atan2(second_disc[0][1] - first_disc[0][1], second_disc[0][0] - first_disc[0][0])

            # Utworzenie dwóch wektorów potrzebnych do rozsunięcia obu dysków, o współrzędnych wartości co najmniej 0.01
            vector = [r * math.cos(angle) + sign(math.cos(angle)) * 0.01, r * math.sin(angle) + sign(math.sin(angle)) * 0.01]
            minus_vector = [-vector[0], -vector[1]]

            # Dyski po przesunięciu o wektor
            moved_first_disc = move_disc(first_disc, vector)
            moved_second_disc = move_disc(second_disc, minus_vector)
            
            # Usunięcie kolizji w przypadku gdy po przesunięciu oba dyski znajdują się w obrębie planszy
            if check_boundaries(moved_first_disc) and check_boundaries(moved_second_disc):
                result[pair[0]] = moved_first_disc
                result[pair[1]] = moved_second_disc
                continue
            # Przesunięcie drugiego dysku o podwójny wektor, w przypadku gdyby klasyczne rozsunięcie 
            # powodowało, że pierwszu dysk zanalazłby się poza obrębem planszy
            if not check_boundaries(moved_first_disc):
                double_minus_vector = [2*minus_vector[0], 2*minus_vector[1]]
                result[pair[1]] = move_disc(second_disc, double_minus_vector)
                continue
            # Przesunięcie pierwszego dysku o podwójny wektor, w przypadku gdyby klasyczne przesunięcie
            # powodowało, że drugi dysk znalazłby się poza obrębem planszy
            if not check_boundaries(moved_second_disc):
                double_vector = [2*vector[0], 2*vector[1]]
                result[pair[0]] = move_disc(first_disc, double_vector)

        # Sprawdzenie czy nadal jakieś dyski są ze sobą w kolizji
        collisions = check_collisions(result)

    return result


# Funkcja tworząca wykresy przedstawiające dyski przed i po usunięciu kolizji
def visualize(discs):
    
    fig, axs = plt.subplots(1, 2)

    for ax in axs:
        ax.set_xlim((-SIZE, SIZE))
        ax.set_ylim((-SIZE, SIZE))
        ax.set_aspect('equal')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
    
    axs[0].set_title('Przed rozsunięciem')
    axs[1].set_title('Po rozsunięciu')

    # Utworzenie listy indeksów dysków, które są w kolizji
    first_indexes  = [pair[0] for pair in check_collisions(discs)]
    second_indexes = [pair[1] for pair in check_collisions(discs)]
    indexes = first_indexes + second_indexes

    for disc in discs:
        # Jeżeli dysk jest w kolizji to zaznaczamy go na czerwono
        if discs.index(disc) in indexes:
            axs[0].add_patch(plt.Circle(disc[0], disc[1], fill=False, color='Red'))
        else:
            axs[0].add_patch(plt.Circle(disc[0], disc[1], fill=False))
    
    spreaded_discs = spread_discs(discs)
    for disc in spreaded_discs:
        # Jeżeli dysk był w kolizji to zaznaczamy go na zielono
        if spreaded_discs.index(disc) in indexes:
            axs[1].add_patch(plt.Circle(disc[0], disc[1], fill=False, color='Green'))
        else:
            axs[1].add_patch(plt.Circle(disc[0], disc[1], fill=False))

    plt.show()


# Funkcja główna
def main():

    discs = get_discs(100)
    visualize(discs)


if __name__ == '__main__':
    main()