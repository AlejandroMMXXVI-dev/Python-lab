# ==========================================
# Python Exercises — 2026-03-23
# ==========================================


# Exercise 01: Interval
# Determines which interval contains the given value.

value = float(input())

if 100 < value:
    print("Fora do Intervalo")
elif 75 < value:
    print("Intervalo (75,100]")
elif 50 < value:
    print("Intervalo (50,75]")
elif 25 < value:
    print("Intervalo (25,50]")
elif 0 <= value:
    print("Intervalo [0,25]")
else:
    print("Fora do Intervalo")


# Exercise 02: Snack Bar
# Calculates the total price based on the product code and quantity.

code, quantity = map(float, input().split())

if code == 1:
    total_price = 4.00 * quantity
elif code == 2:
    total_price = 4.50 * quantity
elif code == 3:
    total_price = 5.00 * quantity
elif code == 4:
    total_price = 2.00 * quantity
elif code == 5:
    total_price = 1.50 * quantity

print(f"Total: R$ {total_price:.2f}")


# Exercise 03: Weighted Average
# Calculates a student's weighted average and determines their final result.

n1, n2, n3, n4 = map(float, input().split())

average = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

print(f"Media: {average:.1f}")

if average >= 7:
    print("Aluno Aprovado")

elif average >= 5:
    print("Aluno em Exame")

    exam_score = float(input())

    print(f"Nota do Exame: {exam_score:.1f}")

    final_average = (average + exam_score) / 2

    if final_average >= 5:
        print("Aluno Aprovado")
    else:
        print("Aluno Reprovado")

    print(f"Media Final: {final_average:.1f}")

else:
    print("Aluno Reprovado")


# Exercise 04: Coordinates
# Determines the quadrant or axis where a point is located.

x, y = map(float, input().split())

if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
