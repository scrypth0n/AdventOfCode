valid_1 = 0
valid_2 = 0

with open("02_input") as file:
    passwords = list(file.readlines())

for line in passwords:
    line = line.split('-')
    minimum = line[0]
    line = line[1].split(' ', 1)
    maximum = line[0]
    line = line[1].split(':')
    searched_char = line[0]
    password = list(line[1])
    count_char = 0

    for char in password:
        if char == searched_char:
            count_char += 1
    minimum = int(minimum)
    maximum = int(maximum)

    if minimum <= count_char <= maximum:
        valid_1 += 1
    if (password[minimum] == searched_char) ^ (password[maximum] == searched_char):  # no +1 because password[0] == ' '
        valid_2 += 1

print('Valid Passwords 01:', valid_1)
print('Valid Passwords 02:', valid_2)