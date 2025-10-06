from utn_fra.datasets import lista_velocidades_pp, lista_poderes_pp

from obtener_pp import (
    obtener_promedio, obtener_indices,
    obtener_indices_debiles)

from mostrar_pp import (
    mostrar_info_personajes
)

def obtener_matriz_filtrada(matriz: list[list], lista_indices: list[int]):
    matriz_filtrada = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],      
    ]

    for indice_col in lista_indices:
        for indice_fila in range(len(matriz)):

            dato = matriz[indice_fila][indice_col]
            matriz_filtrada[indice_fila].append(dato)

    return matriz_filtrada

def filtrar_menos_velocidad(matriz:list[list]):

    indice_elegido = mapear_valor_filtrar('velocidad')
    promedio = obtener_promedio(lista_velocidades_pp, indice_elegido)
    lista_indices = obtener_indices(matriz, indice_elegido, promedio)
    matriz_filtrada = obtener_matriz_filtrada(matriz, lista_indices)

    print(f'El promedio de velocidad es: {promedio}')
    mostrar_info_personajes(matriz_filtrada)


def filtrar_debiles(matriz:list[list]):
    indice_elegido = mapear_valor_filtrar('poder')
    promedio = obtener_promedio(lista_poderes_pp, indice_elegido)
    lista_indices = obtener_indices_debiles(lista_poderes_pp, indice_elegido, promedio)
    matriz_filtrada = obtener_matriz_filtrada(matriz, lista_indices)

    print(f'El promedio de poder es: {promedio}')
    mostrar_info_personajes(matriz_filtrada)

def mapear_valor_filtrar(dato: str):
    indice = None
    match dato:
        case 'nombre':
            indice = 0
        case 'alias':
            indice = 1
        case 'raza':
            indice = 2
        case 'genero':
            indice = 3
        case 'poder':
            indice = 4
        case 'inteligencia':
            indice = 5
        case 'velocidad':
            indice = 6
    return indice