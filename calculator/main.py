#!/usr/bin/env python3.6
from calculator import Calculator


def main():
    cal = Calculator()
    a = 3
    b = 2
    suma = cal.sumar(a, b)
    print(f"Suma de {a} + {b} = {suma}")


if __name__ == "__main__":
    main()
