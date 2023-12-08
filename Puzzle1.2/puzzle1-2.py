import re
total = 0
with open("Puzzle1/input.txt") as file:
    while line := file.readline():
        one = re.search('[0-9]', line).group()
        two = re.search('[0-9]', line[::-1]).group()
        total += int(one + two)
    print(total)