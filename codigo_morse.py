"""
* Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
"""
from os import system

# Diccionario de conversión de texto a código Morse
codigo_morse = {'A': '·−', 'B': '−···', 'C': '−·−·', 'D': '−··', 'E': '·',
                'F': '··−·', 'G': '−−·', 'H': '····', 'I': '··', 'J': '·−−−',
                'K': '−·−', 'L': '·−··', 'M': '−−', 'N': '−·', 'O': '−−−', 'P': '·−−·',
                'Q': '−−·−', 'R': '·−·', 'S': '···', 'T': '−', 'U': '··−',
                'V': '···−', 'W': '·−−', 'X': '−··−', 'Y': '−·−−', 'Z': '−−··',
                }

# Diccionario inverso de conversión de código Morse a texto
texto_morse = {mor: let for let, mor in codigo_morse.items()}

def convertir_morse(text: str) -> str:
    """Convierte una cadena de texto en código Morse.

    Args:
        text (str): El texto a convertir a código Morse.

    Returns:
        str: El texto convertido en código Morse, con cada letra separada por un espacio.
    """
    text = text.upper()
    text_mod = ' '.join(codigo_morse.get(letra, '') for letra in text)
    return text_mod

def convertir_palabra(mor: str) -> str:
    """Convierte una cadena de código Morse en texto.

    Args:
        mor (str): El código Morse a convertir en texto.

    Returns:
        str: El texto traducido del código Morse.
    """
    palabras = mor.split('  ')  # Dos espacios entre palabras
    mor_mod = ''
    for palabra in palabras:
        letras = palabra.split(' ')  # Un espacio entre letras
        for letra in letras:
            if letra in texto_morse:
                mor_mod += texto_morse[letra]
        mor_mod += ' '
    return mor_mod.strip()

# Inicio del programa
print('*' * 50)
print('CONVERTIDOR DE MORSE A PALABRA Y PALABRA A MORSE')
print('*' * 50)

print('Ingrese "T" si desea modificar un texto a morse')
print('Ingrese "m" si desea modificar de morse a texto')

nuevo = ''

while nuevo != 'N':
    elegir = str(input('Su elección: ')).upper()  # Aquí el usuario elige la conversión que desea

    system('cls')  # Limpia la pantalla (en sistemas Windows)

    if elegir == 'T':
        texto = input('Ingrese el texto a convertir a morse: ')
        resultado = convertir_morse(texto)
        print(f'Texto convertido a morse: {resultado}')
    elif elegir == 'M':
        morse = input('Ingrese el código morse a convertir a texto: ')
        resultado = convertir_palabra(morse)
        print(f'Código morse convertido a texto: {resultado}')
    else:
        print('Opción no válida. Por favor, ingrese "T" o "m".')

    nuevo = input('Desea continuar? (Y/N) ').upper()  # Preguntamos al usuario si quiere continuar utilizando el programa
    if nuevo == 'N':
        print('GRACIAS POR UTILIZAR EL PROGRAMA!')
