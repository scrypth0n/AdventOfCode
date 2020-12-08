def value_before_infinity(operations, arguments):
    operations_copy = list(operations)
    line = 0
    value = 0
    while True:
        if operations_copy[line] == 'already passed':
            return value
        if operations_copy[line] == 'nop':
            operations_copy[line] = 'already passed'
            line += 1
        elif operations_copy[line] == 'acc':
            operations_copy[line] = 'already passed'
            value += arguments[line]
            line += 1
        elif operations_copy[line] == 'jmp':
            operations_copy[line] = 'already passed'
            line += arguments[line]


def find_false_jmp_nop_test(operations, arguments):
    line = 0
    value = 0
    while True:
        if operations[line] == 'already passed':
            return [False, False]
        if operations[line] == 'nop':
            operations[line] = 'already passed'
            line += 1
        elif operations[line] == 'acc':
            operations[line] = 'already passed'
            value += arguments[line]
            line += 1
        elif operations[line] == 'jmp':
            operations[line] = 'already passed'
            line += arguments[line]
        elif operations[line] == 'correct execution':
            return [True, value]


def find_false_jmp_nop(operations, arguments):
    for line in range(len(operations) - 1):
        operations_test = list(operations)
        if operations[line] == 'nop':
            operations_test[line] = 'jmp'
        elif operations[line] == 'jmp':
            operations_test[line] = 'nop'
        else:
            continue
        response = find_false_jmp_nop_test(operations_test, arguments)
        if response[0]:
            break

    print(operations[line], 'had to be', operations_test[line], 'on line', str(line) + ':', 'value after execution:',
          response[1])


def make_data():
    with open('08_input') as file:
        file = list(file.readlines())
    operations = []
    arguments = []
    for line in file:
        operations.append(line.split(' ', 1)[0])
        arguments.append(int(line.split(' ', 1)[1]))
    operations.append('correct execution')
    operations = tuple(operations)
    return [operations, arguments]


def main():
    data = make_data()
    print('Value before program run for infinity:', value_before_infinity(data[0], data[1]))
    find_false_jmp_nop(data[0], data[1])


if __name__ == '__main__':
    main()
