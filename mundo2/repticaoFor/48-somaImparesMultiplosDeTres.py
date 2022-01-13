#Faça um programa que calcule a soma entre todos os números que são ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
acum = 0
soma = 0
for c in range(1,501,2):
    if c % 3 == 0 :
        soma += c
        acum += 1
print('A quantidade de números somados foram {} '.format(acum))
print('A soma de todos os 83 valores foi {} '.format(soma))
