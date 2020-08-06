print('Vamos calcular quantos baldes de tinta você terá que comprar!!!')
area = float(input('Qual a área em metros quadrados? '))

#1 balde tem 12 litros, cada litro pinta 3 metros quadrados

baldes = area / 36

if area % 36 == 0:

    baldes = int(area / 36)

    print(f'Terá que comprar {baldes} baldes')

else:

    baldes = int(area / 36) + 1

    print(f'Terá que comprar {baldes} baldes')
