"""
Autor: Pierre Vieira
Data da submissão: 17/01/2019 01:07:41
"""
linha1 = input().split(" ")#formatação para ler os valores na mesma linha
a,b,c = linha1
maiorAB = (int(a)+int(b)+abs(int(a)-int(b)))/2 #pega o maior entre A e B
maiorABC = (int(maiorAB) + int(c) + abs(maiorAB-int(c)))/2 #Como ja temos o maior entre A e B, basta comparar esse resultado com C
print("{} eh o maior".format(int(maiorABC)))
