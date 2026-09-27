# ==========================================
# Python Exercises — 2026-04-06
# ==========================================


# Exercise 01: Salary Adjustment
# Calculates the new salary and adjustment based on salary range.

salary = float(input())

if salary <= 400:
    percentage = 0.15
elif salary <= 800:
    percentage = 0.12
elif salary <= 1200:
    percentage = 0.10
elif salary <= 2000:
    percentage = 0.07
else:
    percentage = 0.04

new_salary = salary + salary * percentage
adjustment = salary * percentage

print(f"Novo Salário: {new_salary:.2f}")
print(f"Reajuste Ganho: {adjustment:.2f}")
print(f"Em percentual: {percentage * 100:.0f} %")


# Exercise 02: Animal
# Identifies an animal based on its classification and diet.

phylum = input()
class_type = input()
diet = input()

if phylum == "vertebrado":
    if class_type == "ave":
        if diet == "carnivoro":
            print("aguia")
        elif diet == "onivoro":
            print("pomba")

    elif class_type == "mamifero":
        if diet == "onivoro":
            print("homem")
        elif diet == "herbivoro":
            print("vaca")

elif phylum == "invertebrado":
    if class_type == "inseto":
        if diet == "hematofogo":
            print("pulga")
        elif diet == "herbivoro":
            print("lagarta")

    elif class_type == "anelideo":
        if diet == "hematofogo":
            print("sanguessuga")
        elif diet == "onivoro":
            print("minhoca")


# Exercise 03: DDD
# Identifies a Brazilian city based on its telephone area code.

ddd = int(input())

cities = {
    61: "Brasília",
    71: "Salvador",
    11: "São Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitória",
    31: "Belo Horizonte"
}

if ddd in cities:
    print(f"Cidade do DDD Inserido: {cities[ddd]}")
else:
    print("DDD não cadastrado")


# Exercise 04: Income Tax
# Calculates the income tax based on progressive tax brackets.

income = float(input())
tax = 0.00

if income <= 2000.00:
    print("Isento")

else:
    income -= 2000.00

    if income <= 1000.00:
        tax = income * 0.08
        print(f"R$ {tax:.2f}")

    else:
        tax = 1000.00 * 0.08
        income -= 1000.00

        if income <= 1500.00:
            tax += income * 0.18
            print(f"R$ {tax:.2f}")

        else:
            tax += 1500.00 * 0.18
            income -= 1500.00

            if income > 0.00:
                tax += income * 0.28
                print(f"R$ {tax:.2f}")
