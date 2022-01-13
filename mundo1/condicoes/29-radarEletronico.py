#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual foi a velocidade : '))

if velocidade >= 80:
    multa = velocidade - 80
    precoDaMulta = multa * 7.00
    print('Você ultrapassou o limite de velocidade, que é de 80 KM/h')
    print('Recebeu uma multa no valor de R${:.2f}'.format(precoDaMulta))
else:
    print('Parabéns você está dentro do limite de velocidade !')
