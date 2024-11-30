"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 5. Faça um Programa que peça os 3 lados de um
triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.
Data: 29/09/21
"""
# Entrada de dados
print("==================================")
print("PROGRAMA QUE CLASSIFICA TRIÂNGULOS")
print("==================================")
print(" ")
print("-Preencha os dados exigidos abaixo-")
print(" ")
lado1 = float(input("Informe o tamanho do primeiro lado desse triângulo: "))#Comando que pede para o usuário digitar o tamanho do primeiro lado
lado2 = float(input("Informe o tamanho do segundo lado desse triângulo: "))#Comando que pede para o usuário digitar o tamanho do segundo lado
lado3 = float(input("Informe o tamanho do terceiro lado desse triângulo: "))#Comando que pede para o usuário digitar o tamanho do terceiro lado
print(" ")

# Processamento de dados
if(lado1+lado2>lado3)and(lado1+lado3>lado2)and(lado2+lado3>lado1):#Comando que verifica se pode ou não formar um triângulo com os dados preenchidos
    if(lado1==lado2)and(lado2!=lado3):#Comando que gera o resultado caso primeiro e segundo lado sejam iguais
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("A soma de quaisquer lados é maior que o outro lado!")
        print("Portanto, pode-se formar um triãngulo com esses três lados.")
        print(" ")
        print("Seria um triãngulo isósceles, pois o primeiro e segundo lado são iguais!")
    elif(lado2==lado3)and(lado3!=lado1):#Comando que gera o resultado caso terceiro e segundo lado sejam iguais
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("A soma de quaisquer lados é maior que o outro lado!")
        print("Portanto, pode-se formar um triãngulo com esses três lados.")
        print(" ")
        print("Seria um triãngulo isósceles, pois o segundo e o terceiro lado são iguais!")
    elif(lado3==lado1)and(lado1!=lado2):#Comando que gera o resultado caso primeiro e terceiro lado sejam iguais
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("A soma de quaisquer lados é maior que o outro lado!")
        print("Portanto, pode-se formar um triãngulo com esses três lados.")
        print(" ")
        print("Seria um triãngulo isósceles, pois o primeiro e terceiro lado são iguais!")
    elif(lado1!=lado2)and(lado2!=lado3):#Comando que gera o resultado caso os três lados sejam diferentes
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("A soma de quaisquer lados é maior que o outro lado!")
        print("Portanto, pode-se formar um triãngulo com esses três lados.")
        print(" ")
        print("Seria um triãngulo escaleno, pois os três lados são diferentes!")
    elif(lado1==lado2)and(lado2==lado3):#Comando que gera o resultado caso os três lados sejam iguais
        print("=========")
        print("RESULTADO")
        print("=========")
        print(" ")
        print("A soma de quaisquer lados é maior que o outro lado!")
        print("Portanto, pode-se formar um triãngulo com esses três lados.")
        print(" ")
        print("Seria um triãngulo equilátero, pois os três lados são iguais!")

else:#Comando que gera resultado quando não se pode formar um triângulo com os três lados dados
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("A soma de dois desses lados é menor que a do outro lado!")
    print("Portanto, não se pode formar um triãngulo com esses três lados.")
