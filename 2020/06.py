def make_group():
    with open('06_input') as file:
        file = list(file.readlines())
    groups = []
    new_group = True
    for person in file:
        person = person.replace('\n', '')
        if person != '':
            if new_group:
                new_group = False
                group = []
            group.append(person)
        else:
            new_group = True
            groups.append(group)
    groups.append(group)
    return groups


def count(groups):
    different_yes_answers = 0
    matching_yes_answers = 0
    for group in groups:
        if len(group) == 1:
            different_yes_answers += len(group[0])
            matching_yes_answers += len(group[0])
            print(group, len(group[0]))
            continue
        all_chars = ''
        for person in group:
            for char in person:
                if char not in all_chars:
                    all_chars += char
        different_yes_answers += len(all_chars)
        chars = all_chars
        for person in group:
            for char in all_chars:
                if char not in person:
                    chars = chars.replace(char, '')
        matching_yes_answers += len(chars)
    print('Count yes answers:', different_yes_answers)
    print('Count matching yes answers:', matching_yes_answers)


def main():
    groups = make_group()
    count(groups)


if __name__ == '__main__':
    main()
