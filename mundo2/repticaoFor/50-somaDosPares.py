# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.
acum = 0
soma = 0
for p in range(1,7):
    number = int(input('Digite o {}º numero : '.format(p)))
    if number % 2 == 0 :
        acum += 1
        soma += number
print('A quantidade de números que são pares é {} a soma total resultou em {} '.format(acum,soma))
