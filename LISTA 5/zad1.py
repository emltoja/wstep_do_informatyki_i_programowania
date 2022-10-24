# Zadanie 1 Lista 5

hexadecimal_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


# Funkcja konwertująca tryplet RGB na format HTML
def convert_rgb_to_HTML(rgb_triplet):
    
    red_byte = convert_decimal_to_hexadecimal(rgb_triplet[0])
    green_byte = convert_decimal_to_hexadecimal(rgb_triplet[1])
    blue_byte = convert_decimal_to_hexadecimal(rgb_triplet[2])
    
    return '#' + red_byte + green_byte + blue_byte


# Funkcja przeliczająca wartość z zakewsu (0, 255) z systemu dziesiętnego na system szesnastkowy
def convert_decimal_to_hexadecimal(decimal_value):
    
    first_half = hexadecimal_values[decimal_value % 16]
    second_half = hexadecimal_values[decimal_value // 16]
    
    return second_half + first_half


print(convert_rgb_to_HTML((51, 51, 51)))

