peso_2 = float(input('Seu peso: '))
altura_2 = float(input('Sua altura: '))


imc = peso_2 / (altura_2 * altura_2)

print(f'{imc:.2f}')

if imc < 18.5:
    print('Magreza')
elif (imc >= 18.5) and (imc <= 29.9):
    print('normal')
elif (imc >= 25) and (imc <= 29.99):
    print('Sobrepeso')

elif (imc >= 30) and (imc <= 39.9):
    print('obesidade')

elif imc > 40:
    print('Obesidade Grave')
else:
    print('Inválido')
