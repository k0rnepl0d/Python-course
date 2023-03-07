import math


def main():
    while True:
        z = float(input('Number 1: '))
        b = float(input('Number 2: '))

        if z < 1:
            x = z / b
        elif z >= 1:
            x = math.sqrt((z * b) ** 3)

        y = -math.pi + math.cos(x ** 3) ** 2 + math.sin(x * 2) ** 3

        print(y)

main()
