from mostrar_pp import mostrar_info_personajes

def obtener_existencias(matriz: list[list]) -> int:
    """Obtiene la cantidad de personajes que se encuentran en la matriz

    Args:
        matriz (list[list]): matriz donde se obtienen todos los datos

    Returns:
        int: retorna la cantidad de personajes en numero entero
    """
    return(len(matriz))

def obtener_existencias_human(lista_razas: list, valor: str) -> list[list]:
    """Obtiene la cantidad de personajes que se encuentran en la matriz los que son raza "human"

    Args:
        matriz (list[list]): matriz donde se obtiene la lista de razas 

    Returns:
        int: Retorna la cantidad de personajes en numero entero
    """
    suma_humans = 0

    for razas in lista_razas:
        if valor in razas:
            suma_humans += 1

    print(f'La suma obtenida de {valor} es: {suma_humans}')

def obtener_existencias_not_human(lista_razas: list, valor: str) -> list[list]:
    """Obtiene la cantidad de personajes que se encuentran en la matriz los que no pertenecen a la raza "human"

    Args:
        lista_razas (list[str]): matriz donde se obtiene la lista de razas 

    Returns:
        int: Retorna la cantidad de personajes en numero entero
    """
    suma_not_humans = 0

    for razas in lista_razas:
        if not valor in razas:
            suma_not_humans += 1

    print(f'La suma obtenida de {valor} es: {suma_not_humans}')

def obtener_existencias_saiyan(lista_razas: list[list], valor: str):
    """Obtiene la cantidad de personajes que se encuentran en la matriz de la raza Saiyan, reutilizando otras funciones

    Args:
        lista_razas (list[list]): Lista que le pasamos de Raza
        valor (str): El valor a buscar que en éste caso es 'Saiyan

    Returns:
        _type_: Retornamos la cantidad mostrandolos con el formato pedido
    """
    auxiliar = obtener_existencias_human(lista_razas, valor)
    mostrar_info_personajes(auxiliar)
    return auxiliar

def obtener_promedio(matriz: list[list], indice_a_buscar: int) -> float:
    """Obtenemos un promedio 

    Args:
        matriz (list[list]): La lista de donde sacamos los datos
        indice_a_buscar (int): De que lista buscamos esos datos

    Returns:
        float: Retornamos el promedio 
    """
    cantidad_elemento = len(matriz)
    suma = 0
    
    for indice in matriz:
        suma += indice

    if cantidad_elemento < 1:
        return 0

    promedio = suma / cantidad_elemento
    return promedio

def obtener_indices(matriz:list[list], indice_a_buscar: int, valor_a_buscar: float):

    lista_indices_encontrados = []

    for indice in range(len(matriz[indice_a_buscar])):
        if matriz[indice_a_buscar][indice] < valor_a_buscar:
            lista_indices_encontrados.append(indice)

    return lista_indices_encontrados

def obtener_indices_debiles(matriz:list[list], indice_a_buscar: int, valor_a_buscar: float):

    lista_indices_encontrados = []

    for indice in range(len(matriz)):
        if matriz[indice] < valor_a_buscar:
            lista_indices_encontrados.append(indice)

    return lista_indices_encontrados