"""
Autor: Pierre Vieira
Data da submissão: 25/02/2020 16:26:40
"""
profundidade_colchao, largura_colchao, altura_colchao = map(int, input().split())
altura_porta, largura_porta = map(int, input().split())
if altura_colchao <= altura_porta and largura_colchao <= largura_porta:  # Colchao em pé com face voltada à porta
    print('S')
elif altura_colchao <= altura_porta and profundidade_colchao <= largura_porta:  # Colchao em pé com face voltada à parede
    print('S')
elif altura_colchao <= largura_porta and profundidade_colchao <= altura_porta:  # Colchao passa na horizontal, mas deitado
    print('S')
elif largura_colchao <= altura_porta and altura_colchao <= largura_porta: # Colchao com face voltada à horizontal
    print('S')
elif largura_colchao <= altura_porta and profundidade_colchao <= largura_porta:  # Colchao deitado com face voltada à parede
    print('S')
elif largura_colchao <= largura_porta and profundidade_colchao <= altura_porta:  # Colchao deitado com face voltada ao chao
    print('S')
else:  # Compra não que vai dá merda
    print('N')
