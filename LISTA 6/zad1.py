# Zadanie 1 Lista 6

"""
    Celem jest znalezienie typu danych, który najlepiej będzie 
    reprezentował dysk na płaszczyznie. 
    Jeżeli taki dysk znajduje sie na płaszczyznie, to możemy go
    rozpatrywać jako okrąg. 

    W takim przypadku do opisania okręgu potrzebujemy dwóch wartości:
        
        Jedną z nich będzie położenie środku okręgu na płaszczyznie.
        Najlepszym wyborem będzie lista, którą można modyfikować
        w przeciwieństwie do krotki.

        Drugą wartością będzie długość promienia okręgu reprezentowana
        przez liczbę zmiennoprzecinkową.

    Tym samym dochodzimy do wniosku, że potrzebujemy 2 elementowej listy,
    gdzie pierwszą wartością będzie inna 2 elementowa lista, a drugą 
    liczba zmiennoprzecinkowa
"""

center = [3, 4] # lista reprezentująca położenie środka okręgu
radius = 5 # Promień okręgu

disc_representation = [center, radius] # Krotka reprezentująca dysk na płaszczyznie