numero = int(input('Digite um numero: '))
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in lista:
    resultado = (lista[number] * numero)
    print('{}x{} = {}'.format(numero, lista[number], resultado))


