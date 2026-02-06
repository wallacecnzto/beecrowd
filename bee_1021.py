entrada = float(input())

notas_de_100 = entrada // 100
sobra_dos_100 = entrada % 100

notas_de_50 = sobra_dos_100 // 50
sobra_dos_50 = sobra_dos_100 % 50

notas_de_20 = sobra_dos_50 // 20
sobra_dos_20 = sobra_dos_50 % 20

notas_de_10 = sobra_dos_20 // 10
sobra_de_10 = sobra_dos_20 % 10

notas_de_5 = sobra_de_10 // 5
sobra_de_5 = sobra_de_10 % 5

notas_de_2 = sobra_de_5 // 2
sobra_de_2 = sobra_de_5 % 2

moedas_de_1 = sobra_de_2 //1.0
sobra_das_moedas_de_1 = sobra_de_2 % 1.0

moedas_de_0_50 = sobra_das_moedas_de_1 // 0.50
sobra_das_moedas_de_0_50 = sobra_das_moedas_de_1 % 0.50

moedas_de_0_25 = sobra_das_moedas_de_0_50 // 0.25
sobra_das_moedas_de_0_25 = sobra_das_moedas_de_0_50 % 0.25

moedas_de_0_10 = sobra_das_moedas_de_0_25 // 0.10
sobra_das_moedas_de_0_10 = sobra_das_moedas_de_0_25 % 0.10

moedas_de_0_05 = sobra_das_moedas_de_0_10 // 0.05
sobra_das_moedas_de_0_05 = sobra_das_moedas_de_0_10 % 0.05

moedas_de_0_01 = sobra_das_moedas_de_0_05 // 0.01

print(f"NOTAS:")
print(f"{int(notas_de_100)} nota(s) de R$ 100.00")
print(f"{int(notas_de_50)} nota(s) de R$ 50.00")
print(f"{int(notas_de_20)} nota(s) de R$ 20.00")
print(f"{int(notas_de_10)} nota(s) de R$ 10.00")
print(f"{int(notas_de_5)} nota(s) de R$ 5.00")
print(f"{int(notas_de_2)} nota(s) de R$ 2.00")

print(f"MOEDAS:")
print(f"{int(moedas_de_1)} moeda(s) de R$ 1.00")
print(f"{int(moedas_de_0_50)} moeda(s) de R$ 0.50")
print(f"{int(moedas_de_0_25)} moeda(s) de R$ 0.25")
print(f"{int(moedas_de_0_10)} moeda(s) de R$ 0.10")
print(f"{int(moedas_de_0_05)} moeda(s) de R$ 0.05")
print(f"{int(moedas_de_0_01)} moeda(s) de R$ 0.01")
