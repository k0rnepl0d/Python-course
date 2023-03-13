import math as mt


def culc(x, y, z):
    v = (1 + mt.sin(x + y) ** 2) / (abs(x - ((2 * y) / (1 + (x ** 2) * (y ** 2))))) * (x ** abs(y) + mt.cos(mt.atan(1 / z)) ** 2)
    print(v)


def main():
    while True:
        x = int(input('x => '))
        y = int(input('y => '))
        z = int(input('z => '))

        culc(x=x, y=y, z=z)


if __name__ == '__main__':
    main()