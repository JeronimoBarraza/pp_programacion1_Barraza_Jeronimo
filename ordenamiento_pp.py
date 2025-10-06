from utn_fra.datasets import (
    lista_razas_pp
)

from obtener_pp import (
    obtener_existencias_not_human,
)

def ordenar_por_menos_inteligente(lista_inteligencia: list[list], modo: str = "menor"):
    lista_numeros = lista_inteligencia
    largo_lista = len(lista_numeros)

    for indice in range(largo_lista):
        for sub_indice in range(indice + 1, largo_lista):

            if lista_numeros[indice] < lista_numeros[sub_indice] and modo == "menor":
                auxiliar = lista_numeros[indice]
                lista_numeros[indice] = lista_numeros[sub_indice]
                lista_numeros[sub_indice] = auxiliar
            elif lista_numeros[indice] > lista_numeros[sub_indice] and modo == "mayor":
                auxiliar = lista_numeros[indice]
                lista_numeros[indice] = lista_numeros[sub_indice]
                lista_numeros[sub_indice] = auxiliar

    print(lista_numeros)
    return lista_numeros

def ordenar_menos_inteligente_not_human(lista_not_human: list[list], modo: str = "menor"):

    lista_not_human = []
    for heroe in lista_razas_pp:
        auxiliar = obtener_existencias_not_human(lista_razas_pp)
        lista_not_human.append(auxiliar)
    not_human = ordenar_por_menos_inteligente(lista_not_human, modo="menor")

    print(not_human)
    return not_human

def ordenar_mas_rapido(lista_velocidades_pp: list[list], modo: str = "mayor"):

    auxiliar = ordenar_por_menos_inteligente(lista_velocidades_pp,modo="mayor")
    return auxiliar