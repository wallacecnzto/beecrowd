tempo_de_viagem = int(input())
velocidade_media = int(input())

distancia = tempo_de_viagem * velocidade_media
qtd_litros = distancia / 12

print(f"{qtd_litros:.3f}")
