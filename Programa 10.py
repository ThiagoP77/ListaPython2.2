"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 10.	Faça um Programa para leitura de três notas
parciais de um aluno. O programa deve calcular a média alcançada
por aluno e presentar:
•	A mensagem "Aprovado", se a média for maior ou igual a 7,
com a respectiva média alcançada;
•	A mensagem "Reprovado", se a média for menor do que 7, c
om a respectiva média alcançada;
•	A mensagem "Aprovado com Distinção", se a média for igual a 10.
Data: 08/10/21
"""

# Entrada de dados
print("=====================================")
print("CALCULADORA DE NOTA MÉDIA E APROVAÇÃO")
print("=====================================")
print(" ")
print("-Preencha os dados exigidos abaixo-")
print(" ")
nota1 = float(input("Informe sua primeira nota: "))#Comando que pede para o usuário inserir sua primeira nota
nota2 = float(input("Informe sua segunda nota: "))#Comando que pede para o usuário inserir sua segunda nota
nota3 = float(input("Informe sua terceira nota: "))#Comando que pede para o usuário inserir sua terceira nota
print(" ")

# Processamento de dados
media_notas = ((nota1+nota2+nota3)/3)#Comando que calcula a média das notas

while(media_notas>10)or(media_notas<0):#Comando que define média menor que 0 ou maior que 10 como inválida
    print("Valor inválido!")
    print("Preecnha os dados corretamente!")
    nota1 = float(input("Informe sua primeira nota: "))#Comando que pede para o usuário inserir sua primeira nota
    nota2 = float(input("Informe sua segunda nota: "))#Comando que pede para o usuário inserir sua segunda nota
    nota3 = float(input("Informe sua terceira nota: "))#Comando que pede para o usuário inserir sua terceira nota
    media_notas = ((nota1+nota2+nota3)/3)#Comando que calcula a média das notas
    print(" ")

if(media_notas>=7)and(media_notas<10):#Comando que calcula aprovação para nota maior que 7 e menor que 10
    status = "Aprovado!"

elif(media_notas<7):#Comando que calcula aprovação para nota menor que 7
    status = "Reprovado!"

elif(media_notas==10):#Comando que calcula aprovação para nota igual a 10
    status = "Aprovado com distinção!"
    
# Saída de dados
print("==========")#Conjunto de comandos que exibem os resultados para o usuário
print("RESULTADOS")
print("==========")
print(" ")
print("Média das três notas: %.2f." %(media_notas))
print("Status: %s" %(status))
