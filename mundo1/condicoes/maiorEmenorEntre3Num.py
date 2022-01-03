#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite o primeiro número : '))
b = int(input('Digite o segundo número : '))
c = int(input('Digite o terceiro número : '))

#Verificando o maior
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

#Verificando o menor
if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

print('O maior foi {} '.format(maior))
print('O menor foi {} '.format(menor))