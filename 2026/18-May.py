# ==========================================
# Python Exercises — 2026-05-18
# ==========================================

# Exercise 01: Population Statistics
# Calculates the total number and percentage of each type of animal.

rabbits = rats = frogs = total = 0

for _ in range(int(input())):
    quantity, animal = input().split()
    quantity = int(quantity)

    total += quantity

    if animal == 'C':
        rabbits += quantity
    elif animal == 'R':
        rats += quantity
    elif animal == 'S':
        frogs += quantity

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {rabbits}')
print(f'Total de ratos: {rats}')
print(f'Total de sapos: {frogs}')
print(f'Percentual de coelhos: {(rabbits / total * 100):.2f} %')
print(f'Percentual de ratos: {(rats / total * 100):.2f} %')
print(f'Percentual de sapos: {(frogs / total * 100):.2f} %')


# Exercise 02: I and J
# Prints the required I and J sequence.

i = 1
j = 7

for _ in range(5):
    for _ in range(3):
        print(f'I={i} J={j}')
        j -= 1

    i += 2
    j = 7
