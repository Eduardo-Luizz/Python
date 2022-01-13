#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

from types import MemberDescriptorType


nota1 = float(input('Digite uma nota : '))
nota2 = float(input('Digite outra nota : '))

media = (nota1 + nota2) / 2

if media >= 7: 
    print('Aprovado com media {}'.format(media))
elif media >= 5 and media <= 6.9:
    print('Recuperação com media {}'.format(media))
else :
    print('Reprovado com media {}'.format(media))
