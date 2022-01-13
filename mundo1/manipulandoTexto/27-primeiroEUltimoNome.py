#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Digite o seu nome : ')).strip()

n = name.split() # pega o nome inteiro e sepera pelos espaços
print(n[0])
print(n[len(n) - 1])
