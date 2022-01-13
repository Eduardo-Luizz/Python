#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

name = str(input('Digite o nome da sua cidade : ')).strip()

print(name[:5].upper() == 'SANTO')