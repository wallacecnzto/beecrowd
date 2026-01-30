idade_em_dias = int(input())

ano = idade_em_dias // 365
resto_da_idade_em_dias = idade_em_dias % 365

mes = resto_da_idade_em_dias // 30
resto_da_idade_em_meses = resto_da_idade_em_dias % 30

dia = resto_da_idade_em_meses

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
