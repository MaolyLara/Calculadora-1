a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
operacao = input('Digite a operação: [+, -, *, /]')

if operacao == '+':
  resultado = a + b 
  print (f'{a} + {b} = {resultado}')
elif operacao == '-':
  resultado = a - b 
  print (f'{a} - {b} = {resultado}')
elif operacao == '*':
  resultado = a * b 
  print (f'{a} * {b} = {resultado}')
elif operacao == '/':
  resultado = a / b 
  print (f'{a} / {b} = {resultado}')
else:
     print('Operacao Ivalida')
  
