with open("03_input") as file:
    mountain = list(file.readlines())
list_line = []
for line in mountain:
    list_character = list(line)
    list_line.append(list_character)

len_line = len(list_line[0]) - 1
number_lines = len(list_line)
trees_multiplication = 1
slopes_to_check = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]  # [right, down]
for slope in slopes_to_check:
    trees = 0
    number_line = 1
    place = 1
    for line in range(int(number_lines / slope[1])):
        if place > len_line:
            place -= len_line
        if list_line[number_line-1][place-1] == '#':
            trees += 1
        number_line += slope[1]
        place += slope[0]
    trees_multiplication *= trees
    print('Right:', slope[0], '   Down:', slope[1], '   Trees:', trees)
print('Trees Multiplication:', trees_multiplication)
