"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 4.	Faça um programa que lê as duas notas parciais
obtidas por um aluno numa disciplina ao longo de um semestre, e
calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
•	  Média de Aproveitamento  Conceito
•	  Entre 9.0 e 10.0        A
•	  Entre 7.5 e 9.0         B
•	  Entre 6.0 e 7.5         C
•	  Entre 4.0 e 6.0         D
•	  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito
correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
ou “REPROVADO” se o conceito for D ou E.
Data: 29/09/21
Atualização: 08/10/21
"""

# Entrada de dados
print("===================================")
print("PROGRAMA QUE VERIFICA SUA APROVAÇÃO")
print("===================================")
print(" ")
print("-Preencha os dados exigidos abaixo-")
print(" ")
nota1 = float(input("Informe sua primeira nota: "))#Comando que pede para o usuário inserir sua primeira nota
nota2 = float(input("Informe sua segunda nota: "))#Comando que pede para o usuário inserir sua primeira nota
print(" ")

# Processamento de dados
media_notas = ((nota1+nota2)/2)#Comando que calcula a média das notas

while(media_notas<0)or(media_notas>10):#Comando que gera o resultado caso o usuário insira valores incorretos
    print("Valor inválido!")
    print("Por favor, preencha os dados corretamente!")
    nota1 = float(input("Informe sua primeira nota: "))
    nota2 = float(input("Informe sua segunda nota: "))
    media_notas = ((nota1+nota2)/2)
    print(" ")
    
if (media_notas>=9)and(media_notas<=10):#Comando que calcula conseito e status caso a média esteja entre 9 e 10
    conceito = "A"
    status_aprovacao = "Aprovado"

elif (media_notas<9)and(media_notas>=7.5):#Comando que calcula conseito e status caso a média esteja entre 7.5 e 9
    conceito = "B"
    status_aprovacao = "Aprovado"

elif (media_notas<7.5)and(media_notas>=6):#Comando que calcula conseito e status caso a média esteja entre 6 e 7.5
    conceito = "C"
    status_aprovacao = "Aprovado"

elif (media_notas<6)and(media_notas>=4):#Comando que calcula conseito e status caso a média esteja entre 4 e 6
    conceito = "D"
    status_aprovacao = "Reprovado"

elif (media_notas<4)and(media_notas>=0):#Comando que calcula conseito e status caso a média esteja entre 0 e 4
    conceito = "E"
    status_aprovacao = "Reprovado"
    
# Saída de dados    
if (media_notas>=0)and(media_notas<=10):#Comando que mostra os resultados para o usuário caso a média esteja entre 0 e 10
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("Primeira nota: %.2f."%(nota1))
    print("Segunda nota: %.2f."%(nota2))
    print("Média das notas: %.2f."%(media_notas))
    print("Conceito: %s."%(conceito))
    print("Status: %s!"%(status_aprovacao))
    
