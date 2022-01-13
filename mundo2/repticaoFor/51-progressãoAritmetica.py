#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiroTermo = int(input('Qual o primeiro termo ? '))
razao = int(input('Qual a razão dessa PA : '))

# calcular o decimo termo de uma PA
decimo = primeiroTermo + (11 - 1) * razao
for p in range(primeiroTermo,decimo,razao):
    print(p)