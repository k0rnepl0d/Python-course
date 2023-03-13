import math as mt


def culc(x, y, z):
    v = (1 + mt.sin(x + y) ** 2) / (abs(x - ((2 * y) / (1 + (x ** 2) * (y ** 2))))) * (x ** abs(y) + mt.cos(mt.atan(1 / z)) ** 2)
    print(v)


def main():
    while True:
        x = int(input('x => '))
        y = int(input('y => '))
        z = int(input('z => '))

        list = []

        list.append(x)
        list.append(y)
        list.append(z)

        for i in list:
            if i == 0:
                print('Одно из чисел равно 0!')
                break

        if x == 1 and y == 1:
            print('Error')
            break

        culc(x=x, y=y, z=z)


if __name__ == '__main__':
    main()
