nome = input("Qual palavra deseja inverter? ")
#Primeiramento o programa transforma o input em uma lista 
separar = list(nome)

#A variavel tamanho armazena o tamanho do input
tamanho = len(separar)

#Logo em seguida o programa retira os ultimos itens da lista e os adicionam em primeiro
for i in range(tamanho):
  remove = separar.pop(-1)
  print(f"{remove}", end="")
