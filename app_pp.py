import os
import funciones_pp as fn
import ordenamiento_pp as ord
import obtener_pp as ob
import mostrar_pp as mos
import filtrar_pp as fil
from menu_principal_pp import menu_principal as menu
from validaciones_pp import validar_numero_entre
from utn_fra.datasets import (
    lista_nombre_heroes_pp, lista_alias_pp,
    lista_razas_pp, lista_generos_pp,
    lista_poderes_pp, lista_inteligencias_pp,
    lista_velocidades_pp
)

matriz_resultante = [
    lista_nombre_heroes_pp, lista_alias_pp,
    lista_razas_pp, lista_generos_pp,
    lista_poderes_pp, lista_inteligencias_pp,
    lista_velocidades_pp
]

def aplicacion(nombres: list, alias: list, razas: list, generos: list, poderes: list, inteligencia: list, velocidades: list):

    corriendo = True
    matriz_cargada = False

    while corriendo:
        menu()
        
        opcion = validar_numero_entre(1,22)
        match opcion: 
            case 1:
                fn.validar_matriz_no_este_vacia(matriz_resultante)
                datos = fn.crear_matriz(nombres, alias, razas, generos, poderes, inteligencia, velocidades)
                matriz_cargada = True
                mensaje = 'La matriz fue cargada con éxito! '
                print(mensaje)
                mos.mostrar_info_personajes(datos)
            case 2:
                if matriz_cargada:
                    fn.agregar_personaje(matriz_resultante)
            case 3:
                if matriz_cargada:
                    fn.validar_matriz_no_este_vacia(matriz_resultante)
                    cantidad = ob.obtener_existencias(nombres)
                    mensaje = f'La cantidad de existencias totales es de: {cantidad}'
                    print(mensaje)
            case 4:
                if matriz_cargada:
                    ob.obtener_existencias_human(razas,'Human')
            case 5:
                if matriz_cargada: 
                   ob.obtener_existencias_not_human(razas, 'Human')
            case 6:
                if matriz_cargada:
                    mos.mostrar_info_personajes(matriz_resultante)            
            case 7:
                if matriz_cargada:
                    ob.obtener_existencias_saiyan(razas, 'Saiyan')
            case 8:
                if matriz_cargada:
                    mos.mostrar_mas_poderoso(poderes, 'mayor')
            case 9:
                if matriz_cargada:
                    pass
            case 10:
                if matriz_cargada:
                    fil.filtrar_menos_velocidad(matriz_resultante)
            case 11:
                if matriz_cargada:
                    fil.filtrar_debiles(matriz_resultante)
            case 12:
                if matriz_cargada:
                    pass
            case 13:
                if matriz_cargada:
                    pass
            case 14:
                if matriz_cargada:
                    pass
            case 15:
                if matriz_cargada:
                    pass
            case 16:
                if matriz_cargada: 
                   ord.ordenar_por_menos_inteligente(inteligencia,modo="menor")
            case 17:
                if matriz_cargada:
                    ord.ordenar_menos_inteligente_not_human(razas,modo="menor")
            case 18:
                if matriz_cargada:
                    pass
            case 19:
                if matriz_cargada:
                    ord.ordenar_mas_rapido(lista_velocidades_pp,'mayor')
            case 20:
                if matriz_cargada:
                    pass
            case 21:
                if matriz_cargada:
                    pass
            case 22:
                corriendo = False
                print("Saliendo...")
        
        if not matriz_cargada:
            print("Primero debes inicializar la matriz en la opcion 1")

        os.system("pause")
        os.system("cls")
    
aplicacion(lista_nombre_heroes_pp, lista_alias_pp, lista_razas_pp, lista_generos_pp, lista_poderes_pp, lista_inteligencias_pp, lista_velocidades_pp)
