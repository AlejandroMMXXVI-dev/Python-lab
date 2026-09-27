# ==========================================
# Python Exercises — 2026-03-30
# ==========================================


# Exercise 01: Triangle or Trapezoid
# Calculates the perimeter of a triangle or the area of a trapezoid.

a, b, c = map(float, input().split())

if a + b > c and a + c > b and b + c > a:
    print(f"Perimetro = {(a + b + c):.1f}")
else:
    print(f"Area = {((a + b) * c / 2):.1f}")


# Exercise 02: Multiples
# Determines whether two numbers are multiples of each other.

a, b = map(float, input().split())

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")


# Exercise 03: Triangle Classification
# Determines whether three sides form a triangle and classifies it
# according to its angles and sides.

a, b, c = sorted(map(float, input().split()), reverse=True)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a ** 2 == b ** 2 + c ** 2:
        print("TRIANGULO RETANGULO")
    elif a ** 2 > b ** 2 + c ** 2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")
