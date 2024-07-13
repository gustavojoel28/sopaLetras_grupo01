import random # Biblioteca necesaria

def crear_sopa(palabras):
    tamano = 10  # Tamaño fijo de 10x10

    # Verifica que todas las palabras ingresadas caben en la sopa de letras
    if any(len(palabra) > tamano for palabra in palabras):
        raise ValueError("El tamaño de la sopa de letras no es suficiente para albergar todas las palabras.")
    
    # Crea una matriz de 10x10 llena de espacios en blanco
    sopa = [[' ' for _ in range(tamano)] for _ in range(tamano)]

    # Colocacion de cada palabra en la sopa de letras
    for palabra in palabras:
        colocada = False
        while not colocada:
            direccion = random.choice(['H', 'V', 'D+', 'D-'])
            if direccion == 'H':
                colocada = colocar_horizontal(sopa, palabra)
            elif direccion == 'V':
                colocada = colocar_vertical(sopa, palabra)
            elif direccion == 'D+':
                colocada = colocar_diagonal_positiva(sopa, palabra)
            elif direccion == 'D-':
                colocada = colocar_diagonal_negativa(sopa, palabra)
    
    # Llena los espacios vacíos con letras aleatorias
    llenar_espacios_vacios(sopa)
    return sopa
#-------------------------------------------------------------------------------------#
def colocar_horizontal(sopa, palabra):
    tamano = len(sopa)
    fila = random.randint(0, tamano - 1)
    col = random.randint(0, tamano - len(palabra))
    
    if all(sopa[fila][col + i] in [' ', palabra[i]] for i in range(len(palabra))):
        for i in range(len(palabra)):
            sopa[fila][col + i] = palabra[i]
        return True
    return False
#-------------------------------------------------------------------------------------#
def colocar_vertical(sopa, palabra):
    tamano = len(sopa)
    fila = random.randint(0, tamano - len(palabra))
    col = random.randint(0, tamano - 1)
    
    if all(sopa[fila + i][col] in [' ', palabra[i]] for i in range(len(palabra))):
        for i in range(len(palabra)):
            sopa[fila + i][col] = palabra[i]
        return True
    return False
#-------------------------------------------------------------------------------------#
def colocar_diagonal_positiva(sopa, palabra):
    tamano = len(sopa)
    fila = random.randint(0, tamano - len(palabra))
    col = random.randint(0, tamano - len(palabra))
    
    if all(sopa[fila + i][col + i] in [' ', palabra[i]] for i in range(len(palabra))):
        for i in range(len(palabra)):
            sopa[fila + i][col + i] = palabra[i]
        return True
    return False
#-------------------------------------------------------------------------------------#
def colocar_diagonal_negativa(sopa, palabra):
    tamano = len(sopa)
    fila = random.randint(len(palabra) - 1, tamano - 1)
    col = random.randint(0, tamano - len(palabra))
    
    if all(sopa[fila - i][col + i] in [' ', palabra[i]] for i in range(len(palabra))):
        for i in range(len(palabra)):
            sopa[fila - i][col + i] = palabra[i]
        return True
    return False
#-------------------------------------------------------------------------------------#
def llenar_espacios_vacios(sopa):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(sopa)):
        for j in range(len(sopa[i])):
            if sopa[i][j] == ' ':
                sopa[i][j] = random.choice(letras)
#-------------------------------------------------------------------------------------#
def mostrar_sopa(sopa):
    for fila in sopa:
        print(' '.join(fila))
#-------------------------------------------------------------------------------------#
if __name__ == "__main__":
    palabras = input("Introduce las palabras separadas por comas: ").split(',')
    sopa = crear_sopa([palabra.strip().upper() for palabra in palabras])
    mostrar_sopa(sopa)
