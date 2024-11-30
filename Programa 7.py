"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 7.	Faça um Programa que peça um número correspondente
a um determinado ano e em seguida informe se este ano é ou não bissexto.
Data: 08/10/21
"""

# Entrada de dados
print("====================================")
print("PROGRAMA QUE IDENTIFICA ANO BISSEXTO")
print("====================================")
print(" ")
ano = int(input("Informe o ano em questão: "))#Comando que pede para o usuário digitar um ano
print(" ")
while(ano<0):#Comando que se repete até o usuário inserir o ano corretamente
    print("Valor inválido!")
    print("Por favor, preencha os dados corretamente!")
    ano = int(input("Informe o ano em questão: "))#Comando que pede para o usuário digitar um ano
    print(" ")
    
# Processamento e saída de dados
if (ano%4==0)and(ano%100!=0)or(ano%400==0):#Comando que verifica se um ano é bissexto e gera o resultado
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("O ano digitado é bissexto!")

else:#Comando que gera o resultado caso o ano não seja bissexto
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("O ano digitado não é bissexto!")

