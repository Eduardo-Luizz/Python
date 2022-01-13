#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.


import math
angulo = float(input('Digite o ângulo que deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o Cosceno de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tang))
