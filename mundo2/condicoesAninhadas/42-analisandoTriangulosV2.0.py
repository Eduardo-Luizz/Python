#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

r1 = int(input('Digite a primeira reta : '))
r2 = int(input('Digite a segunda reta : '))
r3 = int(input('Digite a terceira reta : '))
print('\n')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo !')
    if r1 == r2 == r3 or r2 == r1 == r3 or r3 == r2 == r1 :
        print('EQUILÁTERO, todos os lados iguais.')
        print('\n')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r1 != r3 or r2 == r3 != r1 or r3 == r2 != r1 or r3 == r1 != r2 : 
        print('ISÓSCELES, doi lados iguais um diferente.')
        print('\n')
    else :
        print('ESCALENO, todos os lados diferentes')
        print('\n')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo !')
    print('\n')