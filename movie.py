# classes usada para definir os objetos que iram ser armazenados na
# tabela hash, guardando informacoes dos filmes e dos usuarios
class Filme:

    def __init__(self, titulo, id, generos, media, aval):
        self.titulo = titulo
        self.id = id
        self.generos = generos
        self.media = media
        self.aval = aval

def printFilme(filme):
    print filme.titulo
    print filme.id
    print filme.generos
    print filme.media
    print filme.aval

# FUNCOES PARA MANIPULAR ARQUIVOS MOVIE.CSV && RATING.CSV

def leRating():
    #formato das linhas = userId,movieId,rating,timestamp
    #nomeRating = raw_input("nome do arquivo (rating): ")
    arquivoRating = open("minirating.csv",'r')

    #linha = arquivoRating.readline()
    #arquivoRating.next()
    rating = arquivoRating.read()
    rating = rating.splitlines()
    rating = rating[1:]
    #rating.pop()

    #retorna lista de ratings dos filmes, cada index contendo (userId,movieId,rating,timestamp)
    arquivoRating.close()
    return rating


def leFilmes():
    #formato das linhas = movieId,title,genres
    #nomeMovie = raw_input("nome do arquivo (movies): ")
    arquivoMovie = open("movie.csv", 'r')

    linha = arquivoMovie.readline()
    filmes = arquivoMovie.read()
    filmes = filmes.split('\n')
    filmes.pop()  # remove lista vazia do final

    # retorna lista de filmes dos filmes, cada index contendo (movieId,title,genres)
    arquivoMovie.close()
    return filmes

def mediaFilme(filme,rating):
    # somador das notas encontradas
    # contador de quantas notas foram somadas
    # media = somador/contador
    somador = 0
    contador = 0

    media_e_aval = []

    for fil in rating:
        fil = fil.split(',')
        # compara id de filme recebido (movie.csv) com o do filme do arquivo rating.csv
        if filme == fil[1]:
            somador = somador + float(fil[2])
            contador = contador + 1

    if(contador != 0):
        media = somador/contador
        media_e_aval.append(media)
        media_e_aval.append(contador)
    else:
        media_e_aval.append(0)
        media_e_aval.append(0)

    return media_e_aval


# FUNCOES DE HASHING
def hashing(chave, i, M):
    return (chave + i) % M

# END. FECHADO USANDO LISTAS ENCADEADAS + HASHING ((K+I) % M)
def movieId(filmes,rating):
    tamanho = len(filmes)
    tamanho = int(tamanho/5)

    hashTable = buildHashChaining(tamanho)

    i = 0
    for fil in filmes:
        fil = fil.split(',')

        mevia_e_aval = []
        media_e_aval = mediaFilme(fil[0], rating)

        # PREENCHE ESTRUTURA FILME
        filme = Filme(fil[1], int(fil[0]), fil[2], media_e_aval[0], media_e_aval[1])

        k = hashing(filme.id, i, tamanho)  # faz o hashing usando id do filme, indice atual e modulo

        #if (len(hashTable[k]) > 0):
         #   colisao = colisao + 1
        hashTable[k].append(filme)
    #print "End. fechado (listas encadeadas) para hashing linear " + str(colisao)
    return hashTable

# TABELA HASH COM LISTAS ENCADEADAS
def buildHashChaining(m):
    hashTable = []
    for i in range(m):
        hashTable.append([])

    return hashTable

# FUNCAO DE BUSCA

def buscaHash(id, hashTable):
    k = hashing(id,0,len(hashTable))
    for filme in hashTable[k]:
        if filme.id == id:
            return filme

    return False