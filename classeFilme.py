class Filme:

	def __init__(self,id,generos,media,aval):
		self.id = id
		self.generos = generos
		self.media = media
		self.aval = aval

def leRating():
	#formato das linhas = userId,movieId,rating,timestamp
	nomeRating = raw_input("nome do arquivo (rating): ")
	arquivoRating = open(nomeRating,'r')

	linha = arquivoRating.readline()
	rating = arquivoRating.read()
	rating = rating.split('\n')
	rating.pop()

	#retorna lista de ratings dos filmes, cada index contendo (userId,movieId,rating,timestamp)
	arquivoRating.close()
	return rating


def leFilmes():
	#formato das linhas = movieId,title,genres
	nomeMovie = raw_input("nome do arquivo (movies): ")
	arquivoMovie = open(nomeMovie, 'r')

	linha = arquivoMovie.readline()
	filmes = arquivoMovie.read()
	filmes = filmes.split('\n')
	filmes.pop()  # remove lista vazia do final

	# retorna lista de filmes dos filmes, cada index contendo (movieId,title,genres)
	arquivoMovie.close()
	return filmes

# cria lista de todos os filmes (sem repeticoes)
def criaLista(filmes,rating):
	listaFilmes = []
	for fil in filmes:
		fil = fil.split(',')

		mevia_e_aval = []
		media_e_aval = mediaFilme(fil[0],rating)

		# PREENCHE ESTRUTURA FILME
		filme = Filme(fil[0],fil[2],media_e_aval[0],media_e_aval[1])

		# PREENCHE TABELA HASH
		listaFilmes.append(filme)

	return listaFilmes

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

#def avalFilme(filme):


def printaFilmes(listaFilmes):
	for filme in listaFilmes:
		print filme.id
		print filme.generos
		print filme.media
		print filme.aval
		print


#def imprimeLista(lista):
#	for item in lista:
#		print item
#		print

# cria listas para serem incluidas na hash
listaFilmes = leFilmes()
listaRating = leRating()

# cria lista de estrutura que sera usada na hash
listaFilmes = criaLista(listaFilmes,listaRating)

printaFilmes(listaFilmes)


# chamada filme = Filme(2,[acao,terror,suspense],5.6,10000)
#				  Filme(id,generos,media,avaliacoes)
# id serah chave na tabela hash

 			