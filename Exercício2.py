print('-'*35)
print("Bem vindo a sequência de Fibonacci!")
print('-'*35)
# O programa pede ao usuario que insira o numero da conferencia
n = int(input("Qual numero deseja conferir? "))

# Primeiro coloquei o primeiro e segundo valor da sequencia como sendo o penultimo e ultimo numero
penultimo = 0
ultimo = 1

# Em seguida defini o termo, que vai ser o resultado do calculo e os numeros da sequencia
termo = 0

# Logo depois o programa calcula a sequencia de Fibonacci com os valores definidos
while n > termo:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
if n == 0 or n == 1:
    print('O número faz parte da sequência de Fibonacci.')
elif n == termo:
    print('O número faz parte da sequência de Fibonacci.')
else:
    print('O número digitado não faz parte da sequência de Fibonacci.')
