"""
Este programa proporciona funciones para ordenar palabras según su valor numérico romano.
"""

numeros_romanos = {"i":1,"v":5,"x":10,"l":50,"c":100,"d":500,"m":1000}

def calcular_valor(palabra, indice, valor_anadido, contador):
    """
    Calcula el valor numérico de una cadena de caracteres romanos dentro de la palabra.

    Args:
        palabra (str): La cadena a evaluar.
        indice (int): El índice actual en la cadena.
        valor_anadido (int): El valor acumulado hasta el momento.
        contador (int): Contador para controlar la repetición de símbolos.

    Returns:
        int: El valor numérico de la cadena de caracteres romanos.
    """
    if indice < len(palabra) and palabra[indice] in numeros_romanos:
        letra = palabra[indice]
        valor_letra = numeros_romanos[letra]
        letra_anterior = palabra[indice - 1]
        if indice > 0 and letra_anterior in numeros_romanos:
            valor_letra_anterior = numeros_romanos[letra_anterior]
            if letra in "ixcm" and contador != 2:
                if valor_letra > valor_letra_anterior and letra_anterior in "ixc" :
                    valor_anadido += valor_letra - valor_letra_anterior * 2
                elif letra_anterior in "vld" and contador >= 1:
                    return valor_anadido
                else:
                    valor_anadido += valor_letra
                if letra_anterior == letra:
                    contador += 1
                else:
                    contador = 0
            elif letra in "vld" and letra_anterior != letra:
                if letra_anterior in "ixc" and contador <= 1 and valor_letra > valor_letra_anterior:
                    valor_anadido += valor_letra - valor_letra_anterior * 2
                    contador += 1
                elif valor_letra_anterior > valor_letra:
                    valor_anadido += valor_letra
        else:
            valor_anadido += valor_letra
        valor_anadido = calcular_valor(palabra,indice + 1, valor_anadido, contador)
    return valor_anadido

def posicion_primer_numero_romano(palabra):
    """
    Encuentra la posición del primer carácter romano en una cadena.

    Args:
        palabra (str): La cadena a buscar.

    Returns:
        int: La posición del primer carácter romano, o None si no se encuentra.
    """
    for i, letra in enumerate(palabra):
        if letra in numeros_romanos:
            return i
    return 0

def obtener_numero_palabras(lista_palabras):
    """
    Obtiene el valor numérico romano de cada palabra en una lista.

    Args:
        lista_palabras (list): Una lista de palabras.

    Returns:
        dict: Diccionario {palabra : valor numérico romano}
    """
    diccionario_palabras_romano = {}
    for palabra in lista_palabras:
        palabra_minuscula = palabra.lower()
        indice = posicion_primer_numero_romano(palabra_minuscula)
        valor_romano = calcular_valor(palabra_minuscula, indice, 0, 0)
        diccionario_palabras_romano[palabra] = valor_romano
    return diccionario_palabras_romano


def ordenar(lista_palabras):
    """
    Ordena una lista de palabras por su valor numérico romano.

    Args:
        lista_palabras (list): Una lista de palabras.
    """
    diccionario_palabras = obtener_numero_palabras(lista_palabras)
    diccionario_ordenado = dict(sorted(diccionario_palabras.items(), key=lambda item: item[1]))
    for palabra, valor in diccionario_ordenado.items():
        print(palabra + " - " + str(valor))

palabras = [
    "Ojo",    # 0
    "Civil",    # 104
    "Paco",     # 100
    "Hijo",     # 1 
    "Tóxico",   # 6
    "Camión",   # 100
    "Clave",    # 150
    "Ximena",   # 11
    "Damian",   # 500
    "Lili",     # 51
    "Claudia",  # 150
    "Medallón", # 1000
    "Clima",    # 151
]

ordenar(palabras)
