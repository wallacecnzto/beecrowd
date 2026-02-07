entrada = float(input())

# transforma tudo em centavos (inteiro)
entrada = int(round(entrada * 100))

notas_de_100 = entrada // 10000
sobra_dos_100 = entrada % 10000

notas_de_50 = sobra_dos_100 // 5000
sobra_dos_50 = sobra_dos_100 % 5000

notas_de_20 = sobra_dos_50 // 2000
sobra_dos_20 = sobra_dos_50 % 2000

notas_de_10 = sobra_dos_20 // 1000
sobra_de_10 = sobra_dos_20 % 1000

notas_de_5 = sobra_de_10 // 500
sobra_de_5 = sobra_de_10 % 500

notas_de_2 = sobra_de_5 // 200
sobra_de_2 = sobra_de_5 % 200

moedas_de_1 = sobra_de_2 // 100
sobra_das_moedas_de_1 = sobra_de_2 % 100

moedas_de_0_50 = sobra_das_moedas_de_1 // 50
sobra_das_moedas_de_0_50 = sobra_das_moedas_de_1 % 50

moedas_de_0_25 = sobra_das_moedas_de_0_50 // 25
sobra_das_moedas_de_0_25 = sobra_das_moedas_de_0_50 % 25

moedas_de_0_10 = sobra_das_moedas_de_0_25 // 10
sobra_das_moedas_de_0_10 = sobra_das_moedas_de_0_25 % 10

moedas_de_0_05 = sobra_das_moedas_de_0_10 // 5
sobra_das_moedas_de_0_05 = sobra_das_moedas_de_0_10 % 5

moedas_de_0_01 = sobra_das_moedas_de_0_05 // 1

print("NOTAS:")
print(f"{notas_de_100} nota(s) de R$ 100.00")
print(f"{notas_de_50} nota(s) de R$ 50.00")
print(f"{notas_de_20} nota(s) de R$ 20.00")
print(f"{notas_de_10} nota(s) de R$ 10.00")
print(f"{notas_de_5} nota(s) de R$ 5.00")
print(f"{notas_de_2} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moedas_de_1} moeda(s) de R$ 1.00")
print(f"{moedas_de_0_50} moeda(s) de R$ 0.50")
print(f"{moedas_de_0_25} moeda(s) de R$ 0.25")
print(f"{moedas_de_0_10} moeda(s) de R$ 0.10")
print(f"{moedas_de_0_05} moeda(s) de R$ 0.05")
print(f"{moedas_de_0_01} moeda(s) de R$ 0.01")

