# ==========================================
# Python Exercises — 2026-02-23
# ==========================================


# Exercise 01: Product Cost
# Calculates the total cost of two products.

code_1, quantity_1, price_1 = map(float, input().split())
code_2, quantity_2, price_2 = map(float, input().split())

cost_1 = quantity_1 * price_1
cost_2 = quantity_2 * price_2

total = cost_1 + cost_2

print(f"VALOR A PAGAR: R$ {total:.2f}")


# Exercise 02: Sphere Volume
# Calculates the volume of a sphere from its radius.

radius = float(input())
pi = 3.14159

volume = 4 / 3 * pi * radius ** 3

print(f"VOLUME = {volume:.3f}")


# Exercise 03: Geometric Areas
# Calculates the areas of five different geometric shapes.

a, b, c = map(float, input().split())
pi = 3.14159

triangle = a * c / 2
circle = c ** 2 * pi
trapezoid = (a + b) * c / 2
square = b ** 2
rectangle = a * b

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezoid:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")


# Exercise 04: Largest Number
# Finds the largest of three integers.

def largest(a, b):
    return int((a + b + abs(a - b)) / 2)


a, b, c = map(int, input().split())

print(f"{largest(largest(a, b), c)} eh o maior")


# Exercise 05: Fuel Consumption
# Calculates a vehicle's fuel consumption in kilometers per liter.

distance = int(input())
fuel = float(input())

print(f"{distance / fuel:.3f} km/l")


# Exercise 06: Distance Between Two Points
# Calculates the Euclidean distance between two points.

from math import sqrt

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"{distance:.4f}")
