#Pierre Vieira (2434 - Saldo do Vovô)
linha = input().split()
a, saldo = map(int, linha)
menor_saldo = saldo
while a > 0:
    a -= 1
    valor = int(input())
    saldo += valor
    if saldo < menor_saldo:
        menor_saldo = saldo
print(menor_saldo)