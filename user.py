from movie import *
from tabulate import tabulate

class User:
    def __init__(self,id,aval):
        self.id = id
        self.aval = []
        self.aval = aval

def printaUser(user):
    print "Filmes revisados pelo usuario "+str(user.id)
    headers = ["User_rating","Title","Global_rating","Count"]
    print tabulate(user.aval,headers=headers,stralign='left')

def userId(rating,hashMovieId):

    lastRate = rating[len(rating)-1].split(',')
    tamanho = long(lastRate[0])
    hashUserId = buildHashChaining(tamanho)

    i = 0
    triplaFilme = []

    old = rating[0].split(',')[0]
    for rate in rating:
        rate = rate.split(',')
        if rate[0] == old:
            filme = buscaHash(int(rate[1]),hashMovieId)
            if filme != False:
                triplaFilme.append((rate[2],filme.titulo,str(filme.media), str(filme.aval)))
        else:
            # PREENCHE ESTRUTURA USER
            user = User(old,triplaFilme)
            k = hashing(int(old),i,tamanho)
            old = rate[0]

            triplaFilme = []
            filme = buscaHash(int(rate[1]),hashMovieId)
            if filme != False:
                triplaFilme.append((rate[2],filme.titulo,str(filme.media), str(filme.aval)))

            hashUserId[k].append(user)

    #filme = buscaHash(int(lastRate[1]), hashMovieId)
    #print rate[0]
  #  print old
   # if rate[0] != old:
    #    print "entrou"
     #   triplaFilme = []

    #triplaFilme.append([filme.titulo, lastRate[2], filme.media, filme.aval])
    user = User(rate[0], triplaFilme)
    k = hashing(int(rate[0]), i, tamanho)
    hashUserId[k].append(user)

    return hashUserId

def buscaUser(id,hashUserId):
    k = hashing(int(id),0,len(hashUserId))

    for user in hashUserId[k]:
        if user.id == id:
            return user

    return False

def pesquisaUser(hashUserId):
    print "ITEM 4.2 - TABELA HASH - USER ID"
    print

    while(True):
        id = raw_input("Digite id do usuario ou S para sair:\n")
        if id.upper() == 'S' or id == '':
            break

        user = buscaUser(id,hashUserId)
        if(user != False):
            printaUser(user)
        else:
            print "Usuario nao encontrado"

        print
