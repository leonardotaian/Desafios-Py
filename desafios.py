#1 — Ordenar Títulos
#Desafio:

#O desafio consiste em ordenar uma lista de títulos de livros em ordem alfabética e deixá-los separados por vírgula.

#A lista de títulos é fornecida como uma string chamada “titulos”, onde cada título está em uma nova linha.

titulos = """O Senhor dos Anéis
Harry Potter e a Pedra Filosofal
1984
O Lobo da Estepe
Cem Anos de Solidão
A Metamorfose
A Revolução dos Bichos
Crime e Castigo
Macunaíma"""

lista = titulos.split('\n')

print(lista)

print(lista[0])