'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 281,00 e R$ 700,00 : aumento de 15%
salários entre R$ 701,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1501,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input('Digite o salario do colaborador: '))

if salario <= 280:
    aumento = salario * 0.2
    sal_reajuste = salario+aumento
    print(f'''
    Salario Antes do Reajuste: {salario}
    Percentual de Reajuste: 20%
    Aumento: {aumento}
    Novo Salario: {sal_reajuste}
    ''')
elif salario >= 281 and salario <= 700:
    aumento = salario * 0.15
    sal_reajuste = salario+aumento
    print(f'''
    Salario Antes do Reajuste: {salario}
    Percentual de Reajuste: 15%
    Aumento: {aumento}
    Novo Salario: {sal_reajuste}
    ''')
elif salario >= 701 and salario <= 1500:
    aumento = salario * 0.10
    sal_reajuste = salario+aumento
    print(f'''
    Salario Antes do Reajuste: {salario}
    Percentual de Reajuste: 10%
    Aumento: {aumento}
    Novo Salario: {sal_reajuste}
    ''')
elif salario >= 1501:
    aumento = salario * 0.10
    sal_reajuste = salario+aumento
    print(f'''
    Salario Antes do Reajuste: {salario}
    Percentual de Reajuste: 5%
    Aumento: {aumento}
    Novo Salario: {sal_reajuste}
    ''')
else:
    print('Valor Inválido!')