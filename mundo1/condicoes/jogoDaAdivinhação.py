import random
import time

computador = random.randint(0,5)

print('--=--' * 20)
print('Este é um desafio, tente adivinhar qual número eu escolhi entre 0 e 5 !!!')
print('--=--' * 20)

print(2 * '\n' )
player = int(input('Tente adivinhar o número escolhido pelo computador : '))

print('PROCESSANDO')
time.sleep(4)

if computador == player: 
    print('Parabéns você venceu')
else:
    print('Que pena você perdeu pensei em {} e você disse {} '.format(computador, player))
    