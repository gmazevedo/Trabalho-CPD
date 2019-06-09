from hashtable import *


# FUNCAO PRINCIPAL
def main():

    listaFilmes = leFilmes()
    listaRating = leRating()

    entradas = len(listaFilmes)

    hashTable = hashChaining(listaFilmes,listaRating)

    taxaOcup(hashTable,entradas)

    for lista in hashTable:
        printaFilmes(lista)

main()