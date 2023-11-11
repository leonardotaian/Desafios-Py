import re

# 1 — Ordenar Títulos
# Desafio:

# O desafio consiste em ordenar uma lista de títulos de livros em ordem alfabética e deixá-los separados por vírgula.

# A lista de títulos é fornecida como uma string chamada “titulos”, onde cada título está em uma nova linha.

titulos = """O Senhor dos Anéis
Harry Potter e a Pedra Filosofal
1984
O Lobo da Estepe
Cem Anos de Solidão
A Metamorfose
A Revolução dos Bichos
Crime e Castigo
Macunaíma"""

lista = titulos.split('\n') # separar a lista com a função split, usando como marcador \n (quebra de linha).

lista_ordenada = sorted(lista) # com a lista separada, usamos a função sorted para por em ordem alfabética.

print(lista) # lista desordenada

print(lista_ordenada) # lista ordenada

# Saída lista desordenada:
# ['O Senhor dos Anéis', 'Harry Potter e a Pedra Filosofal', '1984', 'O Lobo da Estepe', 'Cem Anos de Solidão', 'A Metamorfose', 'A Revolução dos Bichos', 'Crime e Castigo', 'Macunaíma']

# Saída lista ordenada:
# ['1984', 'A Metamorfose', 'A Revolução dos Bichos', 'Cem Anos de Solidão', 'Crime e Castigo', 'Harry Potter e a Pedra Filosofal', 'Macunaíma', 'O Lobo da Estepe', 'O Senhor dos Anéis']

#----------------------------------------------------------------------------------------------------------#

# 2 — Palavra mais longa
# Desafio:

# O desafio consiste em criar uma função que irá receber um texto (string) e retornará a palavra mais longa.

# Segue exemplo de texto:

# No meu computador, o Python habita e com ele eu desvendo a lógica infinita, Nas linhas de código encontro o meu ser
# e através da sintaxe posso me conhecer. As funções e métodos são como os versos que em harmonia se unem
# formando universos. E como Pessoa disse somos todos um pouco no Python me encontro e me torno outro louco.
# Louco pela programação e por tudo que ela traz em um mundo digital onde a criatividade jaz.
# Então que o Python seja minha poesia e em cada linha de código eu encontre a sabedoria.

texto = "No meu computador, o Python habita e com ele eu desvendo a lógica infinita, Nas linhas de código encontro o meu ser e através da sintaxe posso me conhecer. As funções e métodos são como os versos que em harmonia se unem formando universos. E como Pessoa disse somos todos um pouco no Python me encontro e me torno outro louco. Louco pela programação e por tudo que ela traz em um mundo digital onde a criatividade jaz. Então que o Python seja minha poesia e em cada linha de código eu encontre a sabedoria."

# Primeiro colocamos o texto dentro de uma variável

texto_separado = re.split(r'\s|,|;|\.', texto) # dividindo o str texto em uma lista usando a função re.split (poderia usar a função split várias vezes colocando 1 argumento a cada uso porém se tem a re.split vamos usar kkk), usando como argumento espaço, virgula, ponto e ponto e vírgula

tamanho_lista = len(texto_separado) # vou usar a função range no laço for, então preciso do quantidade de elementos na lista

palavra_longa = "" # aqui inicio uma variável str para receber a palavra mais longa

for i in range(tamanho_lista): # iniciando o laço for para percorrer todos elementos da lista
    if len(texto_separado[i]) > len(palavra_longa): # aqui verifico se o tamanho da palavra da lista no índice i é maior que a palavra longa
        palavra_longa = texto_separado[i] # caso sim, a var palavra_longa recebe o elemento da lista.

print(palavra_longa)

# Saída palavra_longa:
# Criatividade

#----------------------------------------------------------------------------------------------------------#

