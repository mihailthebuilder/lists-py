"""List exercises"""

numbers = [value for value in range(1, 10 ** 6)]
print(sum(numbers))

odds = list(range(1, 21, 2))
for odd in odds:
    print(odd)
