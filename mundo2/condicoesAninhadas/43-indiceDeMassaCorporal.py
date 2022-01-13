# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:

# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso : '))
altura = float(input('Digite sua altura : '))
print('\n')
imc = peso / (altura * altura)

if imc <= 18.5 :
    print('Abaixo do peso com IMC = {:.2f}'.format(imc))
    print('\n')
elif imc > 18.5 and imc <= 25 :
    print('Peso ideal com IMC = {:.2f}'.format(imc))
    print('\n') 
elif imc > 25 and imc <= 30 :
    print('Sobrepeso com IMC = {:.2f}'.format(imc))
    print('\n')
elif imc > 30 and imc <= 40 :
    print('Obesidade com IMC = {:.2f}'.format(imc))
    print('\n')
elif imc > 40 :
    print('Obesidade mórbida com IMC = {:.2f}'.format(imc))
    print('\n')
