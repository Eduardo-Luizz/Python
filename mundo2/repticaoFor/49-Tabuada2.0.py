#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

number = int(input('Digite um número para obter a tabuada : '))

for t in range(0, 11):
    print(' {} X {} = {} '.format(number, t, number*t))