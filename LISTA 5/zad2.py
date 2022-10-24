# Zadanie 2 Lista 5

# Słownik przyporządkujący cyfrom z systemu szesnastkowego liczby z systemu dziesiętnego
hexadecimal_values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15} 

# Funkcja konwertująca z formatu HTML na tryplet RGB
def convert_HTML_to_RGB(html_color_value):

    html_color_value = html_color_value.upper()
    # Sprawdzenie czy podana wartość jest w formacie HTML
    if html_color_value[0] != "#" or len(html_color_value) != 7:
        return 'Podano wartość w nieprawidłowym formacie'

    # Przekonwertowanie poszczególnych wartości z formatu HTML na odpowiadające im wartości w tryplecie RGB
    red_value = convert_hexadecimal_to_decimal(html_color_value[1:3])
    green_value = convert_hexadecimal_to_decimal(html_color_value[3:5])
    blue_value = convert_hexadecimal_to_decimal(html_color_value[5:7])

    return (red_value, green_value, blue_value)

# Funkcja przeliczająca wartości z zakresu (00, FF) w systemie szesnastkowym na wartości z zakresu (0, 255) w systemie dziesiętnym
def convert_hexadecimal_to_decimal(hex_value):

    first_bit = hexadecimal_values.get(hex_value[0]) * 16
    second_bit = hexadecimal_values.get(hex_value[1])

    return first_bit + second_bit


print(convert_HTML_to_RGB('#ABCDEF'))