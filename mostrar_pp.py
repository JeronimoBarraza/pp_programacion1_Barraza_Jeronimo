import obtener_pp as ob

def mostrar_detalle(lista_info: list[list]) -> list[list]:

    cantidad_elementos = len(lista_info[0])

    for indice_col in range(cantidad_elementos):
        for indice_fila in range(len(lista_info)):

            total = (lista_info[indice_fila][indice_col])

    if len(str(total)) < 15:
        mostrar_info_personajes(total)

def mostrar_poderoso(lista_poderosos: list[list]):
    for indice_fila in range(len(lista_poderosos)):
        dato = ob.obtener_dato_del_indice(lista_poderosos, indice_fila)
        print(f'N° indice: {indice_fila} - Poder: {dato}')

def mostrar_mas_poderoso(lista_poderosos: list, modo: str = 'mayor'):
    aux = None

    for indice in range(len(lista_poderosos)):
        if aux == None or (lista_poderosos[aux] < lista_poderosos[indice] and modo == 'mayor') or\
            (lista_poderosos[aux] > lista_poderosos[indice] and modo == 'menor'):
            aux = indice

            print(f'Los personajes más poderosos son: {lista_poderosos[aux]}')

def mostrar_info_personajes(matriz: list[list]) -> list[list]:
    cantidad_columna = len(matriz[0])

    texto = 'nombre,alias,raza,genero,inteligencia,poder,velocidad\n'
    for indice_columna in range(cantidad_columna):
        dato = ''

        for indice_fila in range(len(matriz)):
            dato = f'{dato}{matriz[indice_fila][indice_columna]}'

            if indice_fila < len(matriz) - 1:
                dato = f'{dato},'

        texto += f'{dato}\n'
    print(texto)