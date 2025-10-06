def menu_principal():

    pantalla = \
    """
    # 1 - Crear Matriz: para ello deberá crear una función que en base a las listas, cree una matriz con los datos para trabajar.

    # 2 - Agregar personaje: Debes poder agregar un personaje a la matriz, los datos a incluir son: Nombre, Alias, Raza, Género, Inteligencia, Poder, Velocidad. 

    # 3 - Existencias: Mostrar la cantidad de personajes que hay en el set de datos.

    # 4 - Existencias personajes Human: Mostrar la cantidad de personajes que sean raza Human o en caso de que tengan una raza compuesta, tengan Human en su raza

    # 5 - Existencias personajes que no sean Human: Mostrar la cantidad de personajes cuya raza no sea Human o no tenga Human como parte de su raza compuesta

    # 6 - Mostrar Detalle: Recorrer la matriz y mostrar la info de todos los personajes truncando los strings a 15 caracteres como máximo. 
          (con una función que acepte ese tipo de matriz) con formato: nombre,alias,raza,género,inteligencia,poder,velocidad

    # 7 - Mostrar Saiyan: Recorrer la matriz y mostrar la info (con una función que acepte ese tipo de matriz) 
          con formato: nombre,alias,raza,género,inteligencia,poder,velocidad solamente de los personajes cuya raza sea Saiyan

    # 8 - Mostrar más poderoso: Determinar cuál o cuáles son los personajes con más poder y mostrar sus datos, junto con la cantidad que poseen

    # 9 - Mostrar más inteligente: Determinar cuál o cuáles son los personajes más inteligentes y mostrar sus datos, junto con la cantidad que poseen

    # 10 - Filtrar Menor velocidad: Filtrar/Buscar y mostrar la info de los personajes que no superen el promedio de velocidad.

    # 11 - Filtrar Débiles: Filtrar/buscar en la matriz todos los personajes cuyo poder no superen el poder de personajes de raza Saiyan.

    # 12 - Filtrar No-Binario Veloces:  Filtrar/buscar en la matriz todos los personajes de género No-Binario que posean la más alta velocidad.

    # 13 - Promedios Inteligencia: Calcular el promedio de inteligencia y poder de los personajes que sean de raza Android.

    # 14 - Filtrar Kryptonian: Solamente de los personajes que NO sean raza Kryptonian, 
           mostrar la info completa de los que superen o igualen el promedio de poder de personajes de raza Kryptonian.

    # 15 - Filtrar Saiyan Power: Mostrar la info de los personajes (que no sean raza Saiyan) cuyos stats estén por debajo del índice de ataque Saiyan, 
           obtenido de la ecuación (promedio poder + promedio inteligencia + promedio velocidad) / 3. 
           Para saber esto, primero deberás calcular el promedio de esos stats de los personajes cuya raza sea Saiyan.

    # 16 - Ordenar por Más Inteligente: Ordenar la matriz según inteligencia DES

    # 17 - Ordenar por Menos Inteligente [not Human]: Ordenar la matriz según inteligencia ASC de personajes cuya raza no sea Human

    # 18 - Ordenar por Más Poder [not Human]: Ordenar la matriz según poder DES de los personajes cuya raza no sea Human

    # 19 - Ordenar por Más Velocidad: Ordenar la matriz según velocidad ASC

    # 20 - Ordenar personalizado: Ordenar la matriz según lo siguiente:
            Todos los personajes deben estar agrupados por Raza
            Cada personaje de cada raza, debe estar ordenado según poder DES en su raza.
            Las Razas en la matriz deben aparecer de forma Alfabética

    # 21 - Trasponer Datos: Trasponer la matriz y mostrar su información prolija 
            con una función que acepte ese tipo de matriz, además debe estar ordenada por Raza ASC.

    # 22 - Salir.
    """

    print(pantalla)

