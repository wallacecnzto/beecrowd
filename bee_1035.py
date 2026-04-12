valores_str = input().split()
valores_int = []

for valor in valores_str:
    valores_int.append(int(valor))

A, B, C, D = valores_int

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")