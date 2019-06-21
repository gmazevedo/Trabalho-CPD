# classe usada para definir os objetos que iram ser armazenados na
# arvore trie, guardando informacoes dos filmes
class Nodo:
    def __init__(self,char,id):
        self.filhos = []
        self.id = id
        self.char = char
        self.counter = 1
        # indica de nodo eh fim de palavra
        self.isEnd = False

def insert(root,palavra,idmovie):

    nodo = root
    #tamPalavra = len(palavra)

    for char in palavra:
        found = False

        # procura char na lista de filhos do nodo atual
        for filho in nodo.filhos:
            #se achou, o nodo aponta para o filho que contem o char
            if filho.char == char:
                filho.counter +=1
                nodo = filho
                found = True
                break

        # se nao encontrou o char, insere um novo filho
        if not found:
            novoNodo = Nodo(char,idmovie)
            nodo.filhos.append(novoNodo)
            # o nodo aponta pro novo filho
            nodo = novoNodo
    # se acabou a palavra, ativa flag de folha e adiciona idmovie ao nodo-folha
    nodo.isEnd = True
    nodo.id = idmovie

def search(root,prefixo):

    nodo = root

    # se o nodo nao possuir filhos, entao nao ha como
    # fazer a busca por prefixo
    if not nodo.filhos:
        return False,0

    for char in prefixo:
        notFound = True

        # percorre a lista de filhos do nodo
        for filho in nodo.filhos:
        # ao achar o char na lista de filhos
        # aponta para o filho encontrado e avanca para o proximo
        # char do prefixo
            if filho.char == char:
                notFound = False
                nodo = filho
                break

            # se nao achou o nodo referente ao char, retorna Falso
        if notFound:
            return False,0
    # retorna true ao achar o prefixo e o contador (indica quantas palavras tem este prefixo)
    return True,nodo.counter



root = Nodo('*',0)
insert(root,"palavra",1)
insert(root,"toystory",2)
insert(root,"duro de matar",3)

tupla = search(root,'toy')

if tupla[0]:
    print "Prefixo encontrado"
    print "Ha "+str(tupla[1])+" palavras com este prefixo"
else:
    print "Prefixo nao encontrado"

tupla = search(root,'duro')

if tupla[0]:
    print "Prefixo encontrado"
    print "Ha "+str(tupla[1])+" palavras com este prefixo"
else:
    print "Prefixo nao encontrado"






