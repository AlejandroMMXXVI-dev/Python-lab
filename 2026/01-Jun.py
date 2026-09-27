# ==========================================
# Python Exercises — 2026-06-01
# ==========================================

# Exercise 01: Average Age
# Calculates the average of all non-negative ages entered.

age = float(input())
total_age = 0
count = 0

while age >= 0:
    total_age += age
    count += 1
    age = float(input())

average = total_age / count

print(f'{average:.2f}')


# Exercise 02: Positive Replacement
# Replaces all non-positive values with 1.

values = []

for i in range(10):
    values.append(int(input()))

    if values[i] <= 0:
        values[i] = 1

for i in range(10):
    print(f'X[{i}] = {values[i]}')


# Exercise 03: Array Fill
# Fills an array with the remainder of each index divided by T.

t = int(input())
values = [i % t for i in range(10)]

for i, value in enumerate(values):
    print(f'N[{i}] = {value}')


# Exercise 04: Smallest Value
# Finds the smallest value and its position in the array.

n = int(input())
values = list(map(int, input().split()))

smallest = min(values)
position = values.index(smallest)

print(f'Menor valor: {smallest}')
print(f'Posição: {position}')
