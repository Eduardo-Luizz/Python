# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

valorProduto = float(input('Qual o valor do produto ? '))

print('Bem vindo sou uma IA, qual a sua forma de pagamento ? ')
print('\n')
print('''
   1 - À vista dinheito/cheque : 10% de desconto
   2 - À vista no cartão : 5% de desconto
   3 - Em até 2x no cartão: preço formal 
   4 - 3x ou mais no cartão: 20% de juros 
   ''')
print('\n')

option = int(input('Qual a opção desejada ? '))

if option == 1 :
   porcentagem = valorProduto * 10 / 100
   desconto = valorProduto - porcentagem
   print('O valor do produro é {:.2f} o desconto foi de {:.2f} então o valor final é {:.2f}'.format(valorProduto, porcentagem, desconto))
elif option == 2 :
   porcentagem = valorProduto * 5 / 100
   desconto = valorProduto - porcentagem
   print('O valor do produro é {:.2f} o desconto foi de {:.2f} então o valor final é {:.2f}'.format(valorProduto, porcentagem, desconto))
elif option == 3 : 
   parcela = valorProduto / 2
   print('O valor do produro é {:.2f} cada parcela custará {:.2f}'.format(valorProduto, parcela))
elif option == 4 :
   quantidadeParcelas = int(input('Quantas parcelas ? '))
   porcentagem = valorProduto * 20 / 100
   aumento = valorProduto + porcentagem
   parcela = aumento / quantidadeParcelas
   print('Sua compra está parcela em {:.2f}x o valor de cada parcela é de {:.2f} '.format(quantidadeParcelas, parcela))
   print('Então sua compra que era de {:.2f} passou a ser {:.2f}'.format(valorProduto, aumento))
else : 
   print('Opção inválida, tente novamente.')


