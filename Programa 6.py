"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 6.	Faça um programa que calcule as raízes de uma equação
do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores
de a, b e c e fazer as consistências, informando ao usuário nas seguintes
situações:
•	Se o usuário informar o valor de A igual a zero, a
equação não é do segundo grau e o programa não deve fazer pedir os demais
valores, sendo encerrado;
•	Se o delta calculado for negativo, a equação não possui raizes
reais. Informe ao usuário e encerre o programa;
•	Se o delta calculado for igual a zero a equação possui apenas
uma raiz real; informe-a ao usuário;
•	Se o delta for positivo, a equação possui duas raiz reais;
informe-as ao usuário;
Data: 08/10/21
"""

# Entrada de dados
print("==========================================")
print("CALCULADORA DE RAÍZ DE EQUADÇÃO QUADRÁTICA")
print("==========================================")
print(" ")
print("-Preencha com os valores dos coeficientes-")
print(" ")
a = float(input("Coeficiente a: "))#Comando que pede para o usuário inserir o valor de a
if(a == 0):#Comando que gera o resultado caso a seja igual a zero
    print(" ")
    print("Como a vale zero, não se trata de uma equação quadrática!")
    print("Programa encerrado!")
elif(a!=0):#Comando que verifica se a é diferente de zero
    b = float(input("Coeficiente b: "))#Comando que pede para o usuário inserir o valor de b
    c = float(input("Coeficiente c: "))#Comando que pede para o usuário inserir o valor de c
    print(" ")
    
# Processamento e saída de dados
if(a != 0):#Comando que verifica se a é diferente de zero
    delta = ((b**2)-(4*a*c))#Comando que calcula o delta
    raiz_de_delta = (delta**0.5)#Comando que calcula a raíz quadrada de delta
    if(delta<0)and(a != 0):#Comando que gera o resultado caso o delta seja negativo
        print("Delta é negativo, portanto não há raízes reais!")
        print("Programa encerrado!")
    elif(delta==0)and(a != 0):#Comando que gera o resultado caso o delta seja zero
        raiz_unica = (-(b)/(2*a))#Comando que calcula a raíz da equação
        print("==========")
        print("RESULTADOS")
        print("==========")
        print(" ")
        print("Como delta vale zero, há somente uma raíz.")
        print("A raíz dessa equação é %.2f."%(raiz_unica))
    elif(delta>0)and(a != 0):#Comando que gera o resultado caso o delta seja positivo
        raiz_um = ((-(b)+raiz_de_delta)/(2*a))#Comando que calcula a primeira raíz da equação
        raiz_dois = ((-(b)-raiz_de_delta)/(2*a))#Comando que calcula a segunda raíz da equação
        if(raiz_um>raiz_dois):#Comando que gera o resultado quando a primeira raíz é a maior
            print("==========")
            print("RESULTADOS")
            print("==========")
            print(" ")
            print("Como delta é maior que zero, há duas raízes reais.")
            print("A primeira raíz é %.2f e a segunda é %.2f." %(raiz_dois, raiz_um))
        elif(raiz_dois>raiz_um):#Comando que gera o resultado quando a segunda raíz é a maior
            print("==========")
            print("RESULTADOS")
            print("==========")
            print(" ")
            print("Como delta é maior que zero, há duas raízes reais.")
            print("A primeira raíz é %.2f e a segunda é %.2f." %(raiz_um, raiz_dois))
