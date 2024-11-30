"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: 2. Faça um programa para o cálculo de uma folha de
pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para
o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas
não é descontado (é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa deverá
pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.
•	Desconto do IR:
•	Salário Bruto até 900 (inclusive) - isento
•	Salário Bruto até 1500 (inclusive) - desconto de 5%
•	Salário Bruto até 2500 (inclusive) - desconto de 10%
•	Salário Bruto acima de 2500 - desconto de 20% Imprima na
tela as informações, dispostas conforme o exemplo abaixo. 
Data: 29/09/21
"""

#Variáveis
porcentagem_sindicato = "(3%)"#Porcentagem descontada pelo sindicato
porcentagem_FGTS = "(11%)"#Porcentagem do FGTS

# Entrada de dados
print("==============================")
print("CALCULADORA DE SALÁRIO LÍQUIDO")
print("==============================")
print(" ")
print("-Preencha os dados exigidos abaixo-")
print(" ")
horas_mensais = float(input("Informe quantas horas você trabalhou nesse referido mês: "))#Comando que pede para o usuário informar quantas horas ele trabalhou durante o mês
ganho_hora = float(input("Informe o valor pago por hora: "))#Comando que pede para o usuário informar quanto ganha por hora
print(" ")

# Processamento de dados
salario_bruto = (horas_mensais*ganho_hora)#Comando que calcula o salário bruto

if (salario_bruto<=900):#Comando que define o IR e seu percentgual caso o salário bruto seja menor ou igual a R$900.00
    imposto_renda = 0
    porcentagem = "(0%)"

elif (salario_bruto>900) and (salario_bruto<=1500):#Comando que define o IR e seu percentgual caso o salário bruto seja maior que R%900.00 e menor ou igual a R$1500.00
    imposto_renda = (salario_bruto*0.05)
    porcentagem = "(5%)"

elif (salario_bruto>1500) and (salario_bruto<=2500):#Comando que define o IR e seu percentgual caso o salário bruto seja maior que R%1500.00 e menor ou igual a R$2500.00
    imposto_renda = (salario_bruto*0.1)
    porcentagem = "(10%)"

elif (salario_bruto>2500):#Comando que define o IR e seu percentgual caso o salário bruto seja maior que R$2500.00
    imposto_renda = (salario_bruto*0.2)
    porcentagem = "(20%)"

sindicato = (salario_bruto*0.03)#Comando que calcula o valor descontado pelo sindicato
FGTS = (salario_bruto*0.11)#Comando que calcula valor do FGTS
desconto_total = (sindicato+imposto_renda)#Comando que calcula o total descontado do salário bruto
salario_liquido = (salario_bruto-desconto_total)#Comando do calcula salário líquido
    
# Saída de dados
print("==========")#Conjunto de comandos que mostram os valores calculados ao usuário
print("RESULTADOS")
print("==========")
print(" ")
print("Salário bruto: R$%.2f." %(salario_bruto))
print("(Descontado) Imposto de renda%s: R$%.2f."%(porcentagem, imposto_renda))
print("(Descontado) Sindicato%s: R$%.2f." %(porcentagem_sindicato, sindicato))
print("(Não tem desconto) FGTS%s: R$%.2f." %(porcentagem_FGTS, FGTS))
print("Total de descontos: R$%.2f." %(desconto_total))
print("Salário líquido: R$%.2f." %(salario_liquido))

