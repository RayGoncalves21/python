''' condições IF, ELIF e ELSE '''

saldo = 1000


status = input('Digite o status ')
valor = int(input('Valor '))

if status == 'GREEN':
    saldo += valor
    print(saldo)

elif status == 'RED':
    saldo -= valor
    print(saldo)

else:
   print('invalido')