valor = float(input())

total_centavos = int(round(valor * 100))

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    qtd = total_centavos // nota
    total_centavos %= nota
    print(f"{qtd} nota(s) de R$ {nota / 100:.2f}")

print("MOEDAS:")
for moeda in moedas:
    qtd = total_centavos // moeda
    total_centavos %= moeda
    print(f"{qtd} moeda(s) de R$ {moeda / 100:.2f}")

