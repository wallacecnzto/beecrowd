valor = int(input())

qtd_de_100 = valor // 100
resto_da_divisao_100 = valor % 100

qtd_de_50 = resto_da_divisao_100 // 50
resto_da_divisao_50 = resto_da_divisao_100 % 50

qtd_de_20 = resto_da_divisao_50 // 20
resto_da_divisao_20 = resto_da_divisao_50 % 20

qtd_de_10 = resto_da_divisao_20 // 10
resto_da_divisao_10 = resto_da_divisao_20 % 10

qtd_de_5 = resto_da_divisao_10 // 5
resto_da_divisao_5 = resto_da_divisao_10 % 5

qtd_de_2 = resto_da_divisao_5 // 2
resto_da_divisao_2 = resto_da_divisao_5 % 2

qtd_de_1 = resto_da_divisao_2 //  1
resto_da_divisao_1 = resto_da_divisao_2 % 1

print(f"{qtd_de_100} nota(s) de R$ 100,00")
print(f"{qtd_de_50} nota(s) de R$ 50,00")
print(f"{qtd_de_20} nota(s) de R$ 20,00")
print(f"{qtd_de_10} nota(s) de R$ 10,00")
print(f"{qtd_de_5} nota(s) de R$ 5,00")
print(f"{qtd_de_2} nota(s) de R$ 2,00")
print(f"{qtd_de_1} nota(s) de R$ 1,00")
