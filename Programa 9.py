"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 9.	Faça um Programa que leia um número inteiro menor
que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
•	Observando os termos no plural a colocação do "e", da
vírgula entre outros. Exemplo:
•	326 = 3 centenas, 2 dezenas e 6 unidades
•	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100,
320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
Data: 08/10/21
"""

# Entrada de dados
print("===================================")
print("PROGRAMA QUE ANALISA NÚMERO INTEIRO")
print("===================================")
print(" ")
numero_inteiro = int(input("Digite um número inteiro: "))#Comando que pede para o usuário inserir um número
print(" ")
while(numero_inteiro>=1000)or(numero_inteiro<0):#Comando que exige um número positivo menor que mil
    print("Valor inválido!")
    numero_inteiro = int(input("Digite um número inteiro (positivo e menor que mil): "))#Comando que pede para o usuário inserir um número
    print(" ")

# Processamento de dados
unidades = int(numero_inteiro%10)#Comando que calcula a quantidade de unidades
centenas = int(numero_inteiro/100)#Comando que calcula a quantidade de centenas
dezenas = int((numero_inteiro-(centenas*100))/10)#Comando que calcula a quantidade de dezenas

# Saída de dados
print("==========")#Conjunto de comandos que exibem os resultados ao usuário
print("RESULTADOS")
print("==========")
print(" ")
print("O número %d possui %d centena(s), %d dezena(s) e %d unidade(s)." %(numero_inteiro, centenas, dezenas, unidades))
