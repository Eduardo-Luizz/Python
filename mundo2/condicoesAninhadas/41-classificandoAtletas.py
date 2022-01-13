#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

print('Me passe seu ano de nascimento, para obter sua categoria.')
from datetime import date

anoNasc = int(input('Qual o ano de nascimento ? '))

#descobrir idade
idade = date.today().year - anoNasc

if idade <= 9 : 
    print('MIRIM com {} anos.'.format(idade))
elif idade <= 14 :
    print('INFANTIL com {} anos.'.format(idade))
elif idade <= 19 :
    print('JÚNIOR com {} anos.'.format(idade))
elif idade <= 25 :
    print('SÊNIOR com {} anos.'.format(idade))
else :
    print('MASTER com {} anos.'.format(idade))
