from hashtable import *


def userId(rating):
    tamanho = rating[len(rating)-1].split(',')
    tamanho = int(tamanho[0])/5

    print tamanho


# FUNCAO PRINCIPAL
def main():

    #listaFilmes = leFilmes()
    listaRating = leRating()

    userId(listaRating)

    """
    entradas = len(listaFilmes)

    hashMovieId = movieId(listaFilmes,listaRating)

    taxaOcup(hashMovieId,entradas)

    for lista in hashMovieId:
        printaFilmes(lista)"""

main()