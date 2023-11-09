
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

