#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

number = int(input('Digite um número inteiro : '))

if number %2==0:
    print('Você digitou o número {} é par'.format(number))
else:
    print('Você digitou o número {} é ímpar'.format(number))
