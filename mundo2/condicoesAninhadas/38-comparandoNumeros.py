# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

number1 = int(input('Digite um número : '))
number2 = int(input('Digite outro número : '))

if number1 > number2 :
    print('O maior é {} '.format(number1))
elif number1 < number2 :
    print('O maior é {} '.format(number2))
elif number1 == number2 :
    print('Não existe maior os dois são iguais')
