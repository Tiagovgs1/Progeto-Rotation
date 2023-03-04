faturamento = [67836.43, 36678.66 ,29229.88, 27165.48, 19849.53]
estados = ["sp", "rj", "mg", "es", "outros"]

#Soma de todos os faturamentos
total_mensal = sum(faturamento)

# Contador da lista de estados 
cont = 0 
# O calculo de percentual 
for calculo in faturamento:
  cont += 1
  calculo = calculo / total_mensal * 100
  
  print(f"Porcentagem de {estados[cont - 1]} {calculo:.2f}")
