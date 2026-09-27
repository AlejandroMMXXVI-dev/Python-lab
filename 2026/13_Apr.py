# ==========================================
# Python Exercises — 2026-04-13
# ==========================================

# Exercise 01: Even Numbers
# Prints all even numbers from 2 to 100.

for number in range(2, 101, 2):
    print(number)


# Exercise 02: Positive Values
# Counts how many of the six input values are positive.

numbers = [float(input()) for _ in range(6)]

positive_count = len([number for number in numbers if number > 0])

print(f'{positive_count} valores positivos')


# Exercise 03: Event Duration
# Calculates the duration between two events.

start_day = int(input().split()[1])
start_hour, start_minute, start_second = map(int, input().split(' : '))

end_day = int(input().split()[1])
end_hour, end_minute, end_second = map(int, input().split(' : '))

start_time = (
    start_day * 24 * 60 * 60
    + start_hour * 60 * 60
    + start_minute * 60
    + start_second
)

end_time = (
    end_day * 24 * 60 * 60
    + end_hour * 60 * 60
    + end_minute * 60
    + end_second
)

duration = end_time - start_time

days = duration // (24 * 60 * 60)
duration %= 24 * 60 * 60

hours = duration // (60 * 60)
duration %= 60 * 60

minutes = duration // 60
seconds = duration % 60

print(f'{days} dia(s)')
print(f'{hours} hora(s)')
print(f'{minutes} minuto(s)')
print(f'{seconds} segundo(s)')
