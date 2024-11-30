"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 1.	As Organizações Tabajara resolveram dar um aumento de
salário aos seus colaboradores e lhe contraram para desenvolver o
programa que calculará os reajustes.
•	Faça um programa que recebe o salário de um colaborador e o
reajuste segundo o seguinte critério, baseado no salário atual:
•	salários até R$ 280,00 (incluindo) : aumento de 20%
•	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
•	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
•	salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser
realizado, informe na tela:
•	o salário antes do reajuste;
•	o percentual de aumento aplicado;
•	o valor do aumento;
•	o novo salário, após o aumento.
Data: 28/09/21
Atualização: 29/09/21
"""

# Entrada de dados
print("========================================")
print("PROGRAMA QUE CALCULA REAJUSTE DE SALÁRIO")
print("========================================")
print(" ")
salario_inicial = float(input("Informe seu salário: "))#Comando que pede para o usuário inserir seu salário atual
print(" ")

# Processamento de dados
if (salario_inicial<=280):#Comando que calcula o aumento e o percentual caso o salário seja menor ou igual a 280 reais
    valor_reajuste = (salario_inicial*0.2)
    percentual = "20%"

elif (salario_inicial>280) and (salario_inicial<=700):#Comando que calcula o aumento e o percentual caso o salário esteja entre 280 e 700 reais
    valor_reajuste = (salario_inicial*0.15)
    percentual = "15%"

elif (salario_inicial>700) and (salario_inicial<=1500):#Comando que calcula o aumento e o percentual caso o salário esteja entre 700 e 1500 reais
    valor_reajuste = (salario_inicial*0.1)
    percentual = "10%"

elif (salario_inicial>1500):#Comando que calcula o aumento e o percentual caso o salário seja maior que 1500 reais
    valor_reajuste = (salario_inicial*0.05)
    percentual = "5%"

salario_final= (salario_inicial + valor_reajuste)#Comando que calcula o salário final

# Saída de dados
print("==========")#Conjunto de comandos que exibe os resultados para o usuário
print("RESULTADOS")
print("==========")
print(" ")
print("Salário inicial: R$%.2f." %(salario_inicial))
print("Percentual de aumento: %s do salário inicial." %(percentual))
print("Valor do aumento: R$%.2f." %(valor_reajuste))
print("Salário final: R$%.2f." %(salario_final))
