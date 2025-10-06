from app_pp import aplicacion

from utn_fra.datasets import (
    lista_nombre_heroes_pp, lista_alias_pp,
    lista_razas_pp, lista_generos_pp,
    lista_poderes_pp, lista_inteligencias_pp,
    lista_velocidades_pp
)

aplicacion(lista_nombre_heroes_pp, lista_alias_pp, lista_razas_pp, lista_generos_pp, lista_poderes_pp, lista_inteligencias_pp, lista_velocidades_pp)

if __name__ == "__main__":
    aplicacion()
