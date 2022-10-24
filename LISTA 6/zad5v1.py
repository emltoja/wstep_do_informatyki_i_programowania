# Zadanie 5 Lista 6.

# Importy
from mojefunkcje import collision, move_disc
import random
import math
import matplotlib.pyplot as plt

# Stała określająca rozmiar planszy na której rozmieszczane są dyski.
# W tym przypadku plansza ma rozmiar 30 x 30.
# (-15, 15) x (-15, 15).
BOUNDARY = 15
# Stała określająca promień dysku
RADIUS = 0.5


# Funkcja obliczająca odległość między środkami dwóch dysków.
def distance(first, second):
    return math.sqrt((first[0][0] - second[0][0])**2 + (first[0][1] - second[0][1])**2)

# Funkcja zwracająca znak wartości (1 dla 0).
def sign(value):
    return 1 if value >= 0 else -1

# Funkcja sprawdzająca czy dany dysk znajduje się w obrębie planszy.
def check_boundaries(disc):
    return True if disc[0][0] + RADIUS <= BOUNDARY and disc[0][0] - RADIUS >= -BOUNDARY \
               and disc[0][1] + RADIUS <= BOUNDARY and disc[0][1] - RADIUS >= -BOUNDARY else False

# Funkcja zwracjąca zadaną liczbę losowo położonych dysków o promieniu 0.5 w obrębie planszy.
def generate_discs(ammount):

    discs = []
    for i in range(ammount):
        x = random.uniform(-BOUNDARY + RADIUS, BOUNDARY - RADIUS)
        y = random.uniform(-BOUNDARY + RADIUS, BOUNDARY - RADIUS)
        discs.append([[x, y], RADIUS])
    return discs

# Funkcja zwracająca listę par dysków, które na siebie nachodzą.
def check_collisions(discs):

    result = []
    for disc in discs:
        for other in discs[discs.index(disc) + 1:]:
            if collision(disc, other):
                result.append((discs.index(disc), discs.index(other)))
    return result

# Funkcja rozsuwająca dyski.
def spread_discs(discs):

    result = discs.copy()
    condition = len(check_collisions(result)) != 0

    # Rozsuwanie dysków powtarza się aż nie zostanie usunięta ostatnia kolizja.
    while condition:

        collisions = check_collisions(result)
        # Rozsuwanie każdej pary dysków, które są ze sobą w kolizji.
        for pair in collisions:

            first_disc = result[pair[0]]
            second_disc = result[pair[1]]

            # Obliczenie wartości potrzebnych do utworzenia wektorów opisujących rozsunięcie dysków w odpowiednim kierunku.
            excess_dist = first_disc[1] + second_disc[1] - distance(first_disc, second_disc) # Odległość o jaką zachodzą na siebie dyski
            r = excess_dist / 2 # Długość wektora potrzebnego do rozsunięcia każdego z dysków
            angle = math.atan2(first_disc[0][1] - second_disc[0][1], first_disc[0][0] - second_disc[0][0]) # Kąt pomiędzy wektorem a osią OX
            
            # Utworzenie wektorów o długości co najmniej 0.01.
            # Jest to po to aby zrekompensować zaokrąglanie do 0 w przypadku gdy dyski zachodzą na siebie w bardzo małym stopniu.
            vector = [r*math.cos(angle) + 0.01 * sign(math.cos(angle)) , r*math.sin(angle) + 0.01 * sign(math.sin(angle))]
            minus_vector = [-r*math.cos(angle) - 0.01 * sign(math.cos(angle)), -r*math.sin(angle) - 0.01 * sign(math.sin(angle))]
            # Wektory potrzebne do przesunięcia tylko jednego dysku, w przypadku gdyby po przesunięciu obu, któryś z nich znajdował się poza planszą
            double_vector = [vector[0] * 2, vector[1] * 2]
            double_minus_vector = [minus_vector[0] * 2, minus_vector[1] * 2]

            # Zastąpienie kolidującej pary, parą rozsuniętą.
            if check_boundaries(move_disc(first_disc, vector)) and check_boundaries(move_disc(second_disc, minus_vector)):
                result[pair[0]] = move_disc(first_disc, vector)
                result[pair[1]] = move_disc(second_disc, minus_vector)
            # Przesunięcie tylko drugiego dysku w przypadku gdy po rozsunięciu obu pierwszy znajdowałby się poza obszarem
            elif not check_boundaries(move_disc(first_disc, vector)):
                result[pair[1]] = move_disc(second_disc, double_minus_vector)
            # Przesunięcie tylko pierwszego dysku w przypadku gdy po rozsunięciu obu drugi znajdowałby się poza
            elif not check_boundaries(move_disc(second_disc, minus_vector)):
                result[pair[0]] = move_disc(first_disc, double_vector)

        # Sprawdzenie czy nadal jakieś dyski są ze sobą w kolizji
        condition = len(check_collisions(result)) != 0

    return result
            

# Funkcja zwracjająca konfiguracje podanej listy dysków.
def get_configuration(discs):

    result = ''
    for disc in discs:
        result += str(disc) + '\n'
    return result

# # Funkcja tworząca wykresy przedstawiające dyski przed i po usunięciu kolizji
def visualize(discs):
    
    fig, axs = plt.subplots(1, 2)

    for ax in axs:
        ax.set_xlim((-BOUNDARY, BOUNDARY))
        ax.set_ylim((-BOUNDARY, BOUNDARY))
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

# Główna Funkcja.
def main():

    discs = generate_discs(100)
    visualize(discs)

main()
