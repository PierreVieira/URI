valor = -1
while valor < 0 or valor > 1000000:
    valor = float(input())
print("NOTAS:")
nota100 = valor//100
acumulado = valor - nota100*100
print("{} nota(s) de R$ 100.00".format(int(nota100)))
nota50 = (acumulado)//50
acumulado = acumulado - nota50*50
print("{} nota(s) de R$ 50.00".format(int(nota50)))
nota20 = acumulado//20
acumulado = acumulado - nota20*20
print("{} nota(s) de R$ 20.00".format(int(nota20)))
nota10 = acumulado//10
acumulado = acumulado - nota10*10
print("{} nota(s) de R$ 10.00".format(int(nota10)))
nota5 = acumulado//5
acumulado = acumulado - nota5*5
print("{} nota(s) de R$ 5.00".format(int(nota5)))
nota2 = acumulado//2
acumulado = acumulado - nota2*2
print("{} nota(s) de R$ 2.00".format(int(nota2)))
print("MOEDAS:")
moeda1 = acumulado//1
acumulado = acumulado - moeda1*1
print("{} moeda(s) de R$ 1.00".format(int(moeda1)))
acumulado = int(acumulado *100)#pulo do gato
moeda50 = acumulado//50
acumulado = acumulado - moeda50*50
print("{} moeda(s) de R$ 0.50".format(int(moeda50)))
moeda25 = acumulado//25
acumulado = acumulado - moeda25*25
print("{} moeda(s) de R$ 0.25".format(int(moeda25)))
moeda10 = acumulado//10
acumulado = acumulado - moeda10*10
print("{} moeda(s) de R$ 0.10".format(int(moeda10)))
moeda5 = acumulado//5
acumulado = acumulado - moeda5*5
print("{} moeda(s) de R$ 0.05".format(int(moeda5)))
moeda01 = acumulado//1
acumulado = acumulado - moeda01*1
print("{} moeda(s) de R$ 0.01".format(int(moeda01)))
