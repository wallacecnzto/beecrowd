entrada = input().split()

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

maior_entre_AB = int((a + b + abs(a - b)) / 2)
maior_entre_AC = int((a + c + abs(a - c)) / 2)
maior_entre_BC = int((b + c + abs(b - c)) / 2)

maiores = [maior_entre_AB, maior_entre_AC, maior_entre_BC]

maior = max(maiores)

print(f"{maior} eh o maior")