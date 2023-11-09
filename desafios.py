# A ideia desses pequenos desafios é usar somente a documentação oficial da linguagem para resolver, isolando o uso de códigos prontos e dicas, apenas no que se refere a lógica e uso produtivo de funções e bibliotecas que no meu ver é de suma importância para desenvolver ou analisar um código complexo e extenso.

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

lista = titulos.split('\n')

#print(lista) = virou lista

#print(lista[0]) = da pra acessar linha por linha

#print(len(lista)) = 9