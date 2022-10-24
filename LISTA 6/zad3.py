# Zadanie 3 Lista 6

def move_disc(disc, vector):
    
    # Obliczenie nowego położenia dysku po przesunięciu o wektor
    new_center = (disc[0][0] + vector[0], disc[0][1] + vector[1])

    return [new_center, disc[1]]

print(move_disc([[1, 2], 3], (4, -2)))