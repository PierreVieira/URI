"""
Autor: Pierre Vieira
Data da submissão: 17/01/2019 00:24:37
"""
linha1 = input().split(" ")
linha2 = input().split(" ")
ax, ay, az = linha1
bx, by, bz = linha2
print("VALOR A PAGAR: R$ {:.2f}".format(int(ay)*float(az) + int(by)*float(bz)))
