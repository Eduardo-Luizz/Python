# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valorDaCasa = int(input('Qual é o valor da casa : '))
print('=-' * 20)
salarioDoComprador = int(input('Qual é o salário do comprador : '))
print('=-' * 20)
anosFinanciamento = int(input('Quanto anos de financiamento : '))
print('=-' * 20)
print('\n')

#Transformando os anos de financiamento em meses
transfAnosEmMeses = anosFinanciamento * 12

#calculando a prestaçao mensal
prestacaoMensal = valorDaCasa / transfAnosEmMeses

#calcular 30% do salario 
porcentagemSalario = salarioDoComprador * 30 / 100

if porcentagemSalario > prestacaoMensal :
    print('Para pagar uma casa de {} em {} anos a prestação mensal será de {:.2f} ! '.format(valorDaCasa, anosFinanciamento, prestacaoMensal))
    print('=-' * 20)
    print('30 % do seu salário é R${}' .format(porcentagemSalario))
    print('=-' * 20)
    print('Empréstimo pode ser concedido')
else :
    print('Para pagar uma casa de {} em {} anos a prestação mensal será de {:.2f} ! '.format(valorDaCasa, anosFinanciamento, prestacaoMensal))
    print('=-' * 20)
    print('30 % do seu salário é R${}' .format(porcentagemSalario))
    print('=-' * 20)
    print('Empréstimo NÃO PODE SER CONCEDIDO')
    