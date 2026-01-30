tempo_em_segundos = int(input())

# 1 hora == 3.600 segundos

horas = tempo_em_segundos // 3600
resto_de_horas = tempo_em_segundos % 3600

minutos = resto_de_horas // 60
resto_em_minutos = resto_de_horas % 60

segundos = resto_em_minutos

print(f"{horas}:{minutos}:{segundos}")
