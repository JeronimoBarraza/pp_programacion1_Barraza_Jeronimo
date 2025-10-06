def validar_numero(numero_min: int, numero_max: int, dato_a_validar: str = 'Likes') -> int:
    """En esta funcion validamos un numero 

    Args:
        numero_min (int): Numero minimo
        numero_max (int): Numero maximo
        dato_a_validar (str, optional): El numero a validar

    Returns:
        int: Retornamos el numero válido
    """
    num_str = input(f"Ingrese un numero entre la cantidad de [{numero_min} - {numero_max}]: ")

    if not num_str.isdigit() or not (numero_min <= int(num_str) <= numero_max):
        print(f'Numero incorrecto, ingrese otro numero de nuevo! entre [{numero_min} - {numero_max}]: ')
        num_str = validar_numero(numero_min, numero_max)
    
    numero = int(num_str)
    return numero

def validar_texto(dato_a_validar: str) -> str:
    """En ésta función validamos un texto 

    Args:
        dato_a_validar (str): Texto a validar, utilizando la recursión

    Returns:
        str: Retornamos el texto válido
    """
    texto = input(f"Ingrese un texto: ")

    if texto == '':
        print("Texto vacío, el texto debe tener al menos un caracter: ")
        texto = validar_texto(dato_a_validar)
    return texto

def validar_numero_entre(minimo: int, maximo: int) -> int:
    """ Esta función válida un número que esté en el rango entre el mínimo y el máximo

    Args:
        minimo (int): El número mínimo
        maximo (int): El número máximo 

    Returns:
        int: Retorna el número válido entre el mínimo y el máximo
    """
    numero_str = input('Ingrese un número válido entre [1 - 22]: ')

    if not (minimo <= int(numero_str) <= maximo):
        print("ERROR! escriba nuevamente un numero: ")
        numero_str = validar_numero_entre(minimo,maximo)
        
    numero_str_int = int(numero_str)

    return numero_str_int


def validar_matriz_no_este_vacia(matriz: list[list]) -> bool:

    if matriz == 0:
        print("Primero debes inicializar la matriz")
    else: 
        print("La matriz está inicializada")