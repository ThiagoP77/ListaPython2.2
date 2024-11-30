"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 8.	Faça um Programa que peça
uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
Data: 08/10/21
"""

# Entrada de dados
print("==========================")
print("PROGRAMA QUE VERIFICA DATA")
print("==========================")
print(" ")
print("-Preencha os dados exigidos abaixo-")
print(" ")
dia = int(input("Informe o dia: "))#Comando que pede para o usuário inserir o dia
mes = int(input("Informe o mês: "))#Comando que pede para o usuário inserir o mês
ano = int(input("Informe o ano: "))#Comando que pede para o usuário inserir o ano
print(" ")

# Processamento de dados
if(mes>12)or(dia>31)or(mes<=0)or(dia<=0)or(ano<0):#Comando que verifica se o dia, o mês e o ano estão entre os números válidos
    print("==========")
    print("RESULTADOS")
    print("==========")
    print(" ")
    print("A data digitada é inválida!")

elif(mes>0)and(mes<=12)and(dia>0)and(dia<=31)and(ano>0):#Comando que gera o resultado quando mês, dia e ano estão entre os números válidos
    if(mes==4)or(mes==6)or(mes==9)or(mes==11):#Comando que gera o resultado para os meses de abril, junho, setembro e novembro
        if(dia>0)and(dia<=30):#Comando que gera o resultado quando o dia é válido
            print("==========")
            print("RESULTADOS")
            print("==========")
            print(" ")
            print("A data digitada é válida!")
        elif(dia>30):#Comando que gera o resultado quando o dia não é válido
            print("==========")
            print("RESULTADOS")
            print("==========")
            print(" ")
            print("A data digitada é inválida!")
    elif(mes==1)or(mes==3)or(mes==5)or(mes==7)or(mes==8)or(mes==10)or(mes==12):
        if(dia<=31):#Comando que gera o resultado quando o dia é válido
            print("==========")
            print("RESULTADOS")
            print("==========")
            print(" ")
            print("A data digitada é válida!")
        else:#Comando que gera o resultado quando o dia não é válido
            print("==========")
            print("RESULTADOS")
            print("==========")
            print(" ")
            print("A data digitada é inválida!")
    elif(mes==2):#Comando que gera o resultado para o mês de fevereiro
        if(dia==29):#Comando que gera o resultado quando o dia é 29
            if(ano%4==0)and(ano%100!=0)or(ano%400==0):#Comando que verifica se o ano é bissexto e gera o resultado
                print("==========")
                print("RESULTADOS")
                print("==========")
                print(" ")
                print("A data digitada é válida!")
            else:#Comando que gera o resultado se o ano não for bissexto
                print("==========")
                print("RESULTADOS")
                print("==========")
                print(" ")
                print("A data digitada é inválida!")
        elif(dia<=28):#Comando que gera o resultado quando o dia é válido
            print("==========")
            print("RESULTADOS")
            print("==========")
            print(" ")
            print("A data digitada é válida!")
        elif(dia>29):#Comando que gera o resultado quando o dia não é válido
            print("==========")
            print("RESULTADOS")
            print("==========")
            print(" ")
            print("A data digitada é inválida!")
