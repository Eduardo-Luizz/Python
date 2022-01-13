#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

number1 = int(input('Digite um número : '))
print('O número digitado foi {} , seu antecessor é {} e seu sucessor {} .'.format(number1, (number1 - 1), (number1 + 1)))
