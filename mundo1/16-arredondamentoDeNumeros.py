#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
number = float(input('Digite um número : '))
print('O valor digitado foi {}, sua parte inteira é de {}.'.format(number, trunc(number)))
