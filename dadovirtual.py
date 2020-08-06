import random

def lados_6():

    op = [1, 2, 3, 4, 5, 6]

    print(random.choice(op))

def lados_16():

    op = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    print(random.choice(op))

def lados_20():

    op = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15, 16, 17, 18, 19, 20]

    print(random.choice(op))

def main():

    print('Qual desses dados você escolhe: ')

    lados = int(input('|1| - 6 lados\n\n|2| - 16 lados\n\n|3| - 20 lados\n\n'))

    if lados == 1:

        lados_6()
    
    
    elif lados == 2 :

        lados_16()

    else:

        lados_20()



main()