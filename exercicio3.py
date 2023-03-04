valores_faturamento = [22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 
18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]

# Primeiro removi os 0 da lista para achar os valores pedidos
remover_valor = 0

# A variável minha_lista recebe os valores da lista que são diferente de 0
minha_lista = [valor for valor in valores_faturamento if valor != remover_valor]

# O programa calculou a média dos valores da lista sem o 0
media = sum(minha_lista) / len(minha_lista)

# A variavel acima_da_media encontra somente os valores que estão acima da média
acima_da_media = [teste for teste in valores_faturamento if teste > media]

print(f"O menor valor de faturamento ocorrido em um dia do mês é R${min(minha_lista): .2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês é R${max(minha_lista): .2f}")
print(f"São {len(acima_da_media)} numeros que estão acima da média de R${media: .2f}")
