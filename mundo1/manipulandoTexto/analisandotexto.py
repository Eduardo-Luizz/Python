 #Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

name = str(input('Digite o seu nome : ')).strip()
print('Nome em maiúscula = {} '.format(name.upper()))
print('Nome em minúscula = {} '.format(name.lower()))

print('Quantas letras ao todo = {} '.format(len(name) - name.count(' '))) # eliminou o espaço do meio 

separa = name.split()
print('Quantas letras tem o primeiro nome = {} '.format(separa[0], len(separa[0])))

