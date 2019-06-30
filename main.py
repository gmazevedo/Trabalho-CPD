from movie import *
from user import *

# FUNCAO PRINCIPAL
def main():

    listaFilmes = leFilmes()
    listaRating = leRating()

    #userId(listaRating)


    #entradas = len(listaFilmes)

    hashMovieId = movieId(listaFilmes,listaRating)
    hashUserId = userId(listaRating,hashMovieId)

    print
    print "TABELA HASH - MOVIE ID"
    print
    #for lista in hashMovieId:
     #   for filme in lista:
      #      printFilme(filme)
    pesquisaUser(hashUserId)


main()