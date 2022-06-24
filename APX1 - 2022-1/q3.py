import re

# Nas letras a, b, c e d, como não foi pedido para mostrar nada no console, apenas retornei ao valores, sem mostrar mensagens ou valores.

# Na letra e, parece que o exemmplo de entrada e saída não está certo quanto ao cálculo de juros. Aparentemente o cálculo foi feito com 10 parcelas e não 12, como está no exemplo. Mantive a minha lógica e, para as entradas fornecidas no exemplo, as saídas estão diferentes do exemplo, mas de acordo com os cálculos.

# Questão 3 a)

def isFloat(num):
  if not containsLetterOrSymbol(num):
    count = sum(map(lambda x : 1 if '.' in x else 0, num))
    return count <= 1
  return False

def containsLetterOrSymbol(value):
  if bool(re.search('^[0-9.]*$', value)):
    return False
  return True

print(isFloat(input()))

# Questão 3 b)

def toFloat(num):
  if not isFloat(num):
    count = sum(map(lambda x : 1 if '.' in x else 0, num))
    char = ''
    position = 0

    for i in range(len(num)):
      if not bool(re.search('^[0-9.]*$', num[i])):
        char = num[i]
        position = i + 1
        break    

    if not char and count == 0:
        print(f'Você digitou errado, {num} é um inteiro.') 
    else:
      print(f'Há mais do que um ".".') if count > 1 else print(f'Você digitou errado, {num} não é do tipo float. Na posição {position} há o caractere {char}.')

  else:
    num = float(num)
    return num


toFloat(input())

# Questão 3 c)

def USDtoBRL(value, rate):
  if isFloat(value):
    value = float(value)
    rate = float(rate)
    total = value*rate
    print(f'O valor {value} USD com taxa {rate} vai para {total:.3f} BRL.')
    return total

USDtoBRL(input(), input())

# Questão 3 d)

def discount(value):
  value = format(value - value * 0.15, '.3f')
  return value

discount(USDtoBRL(input(), input()))

# Questão 3 e)

def payment(value, installments):
  installments = int(installments)
  if installments == 1:
    total = float(discount(value))
    print(f'Você ganhou 15% de desconto, portanto, de {value} BRL, você vai pagar {total:.2f} BRL.')

  elif installments > 1:
    eachPayment = value / installments
    for i in range(installments):
      eachPayment += eachPayment * 0.05
    total = eachPayment * installments

    print(f'Pagando em {installments} parcelas, com 5% de juros ao mês, você pagará {eachPayment:.2f} BRL por mês, sendo o total de {total:.2f} BRL.')

payment(USDtoBRL(input(), input()), input('Em quantas vezes você quer comprar o produto?\n'))