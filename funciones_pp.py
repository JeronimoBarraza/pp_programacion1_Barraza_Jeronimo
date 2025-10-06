from utn_fra.datasets import (
    lista_nombre_heroes_pp, lista_alias_pp,
    lista_razas_pp, lista_generos_pp,
    lista_poderes_pp, lista_inteligencias_pp,
    lista_velocidades_pp
)

from validaciones_pp import validar_texto, validar_numero

def crear_matriz(lista_nombre_heroes_pp, lista_alias_pp, lista_razas_pp, lista_generos_pp, lista_poderes_pp, lista_inteligencias_pp, lista_velocidades_pp):
    """Permite crear una matriz a partir de las listas de datos de cada personaje

    Args:
        lista_nombre_heroes_pp (list[str]): Lista con los nombres de los héroes.
        lista_alias_pp (list[str]): Lista con los alias de los héroes.
        lista_razas_pp (list[str]): Lista con las razas de los héroes.
        lista_generos_pp (list[str]): Lista con los géneros de los héroes.
        lista_poderes_pp (list[int]): Lista con los valores de poder.
        lista_inteligencias_pp (list[int]): Lista con los valores de inteligencia.
        lista_velocidades_pp (list[int]): Lista con los valores de velocidad.

    Returns:
        list[list]: Una matriz (lista de listas) donde cada sublista representa una característica de los personajes.
    """
    matriz = [
        lista_nombre_heroes_pp,
        lista_alias_pp,
        lista_razas_pp,
        lista_generos_pp,
        lista_poderes_pp,
        lista_inteligencias_pp,
        lista_velocidades_pp
    ]
    return matriz

def agregar_personaje(matriz: list[list]):
    """Agrega informacion de un personaje nuevo a la matriz

    Args:
        matriz (list[list]): matriz donde se obtienen todos los datos cargados 
    """
    lista_datos = [
        validar_texto('Jerónimo'),
        validar_texto('Jero'),
        validar_texto('Humano'),
        validar_texto('Masculino'),
        validar_numero(numero_min=0, numero_max=100, dato_a_validar=50),
        validar_numero(numero_min=0, numero_max=100, dato_a_validar=51),
        validar_numero(numero_min=0, numero_max=100, dato_a_validar=52)
    ]

    for indice in range(len(lista_datos)):
        matriz[indice].append(lista_datos[indice])
        print(matriz[indice])