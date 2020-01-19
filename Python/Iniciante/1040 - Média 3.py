"""
Autor: Pierre Vieira
Data da submissão: 25/01/2019 00:11:41
"""
linha = input().split(" ")
A, B, C, D = linha
a = 2*float(A)
b = 3*float(B)
c = 4*float(C)
d = float(D)
media = (a+b+c+d)/10
print("Media: {:.1f}".format(media))
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    media = (media + nota_exame)/2
    print("Nota do exame: {:.1f}".format(nota_exame))
    if media >= 5:
        print("Aluno aprovado.\nMedia final: {:.1f}".format(media))
    else:
        print("Aluno reprovado.\nMedia final: {:.1f}".format(media))
