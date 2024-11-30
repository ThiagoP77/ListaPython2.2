"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 3.	Faça um Programa que leia um número e exiba o
dia correspondente da semana. (1-Domingo, 2- Segunda,
etc.), se digitar outro valor deve aparecer valor inválido.
Data: 29/09/21
Atualização: 08/10/21
"""

# Entrada de dados
print("===============================================")
print("PROGRAMA QUE RELACIONA NÚMERO COM DIA DA SEMANA")
print("===============================================")
print(" ")
numero = float(input("Digite um número: "))#Comando que pede para o usuário inserir um número
print(" ")
while (numero != 1)and(numero != 2)and(numero != 3)and(numero != 4)and(numero != 5)and(numero != 6)and(numero != 7):#Comando que gera o resultado caso o usuário digite um número inválido
    print("Valor inválido!")
    numero = float(input("Digite outro número: "))
    print(" ")

# Processamento de dados
if (numero == 1):#Comando que gera o resultado caso o número digitado seja 1
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O dia da semana correspondente a 1 é o domingo!")

elif (numero == 2):#Comando que gera o resultado caso o número digitado seja 2
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O dia da semana correspondente a 2 é a segunda-feira!")

elif (numero == 3):#Comando que gera o resultado caso o número digitado seja 3
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O dia da semana correspondente a 3 é a terça-feira!")

elif (numero == 4):#Comando que gera o resultado caso o número digitado seja 4
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O dia da semana correspondente a 4 é a quarta-feira!")

elif (numero == 5):#Comando que gera o resultado caso o número digitado seja 5
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O dia da semana correspondente a 5 é a quinta-feira!")
    
elif (numero == 6):#Comando que gera o resultado caso o número digitado seja 6
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O dia da semana correspondente a 6 é a sexta-feira!")

elif (numero == 7):#Comando que gera o resultado caso o número digitado seja 7
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("O dia da semana correspondente a 7 é o sábado!")
