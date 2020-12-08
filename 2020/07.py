def make_data():
    with open("07_input") as f:
        file = f.readlines()
    all_bags = {}
    for line in file:
        key_color = line.split(' bags contain ', 1)[0]
        value_color = line.split('contain ', 1)[1].replace(' bags', '').replace('.\n', '').split(', ')
        values_color = {}                       # replace('bags') und replace('bag') on different lines, to safe a line
        for value in value_color:
            values_color.update({value.replace(' bag', '').split(' ', 1)[1]: value.split(' ', 1)[0]})
        all_bags.update({key_color: values_color})
    return all_bags


def bags_with_searched_inner_bag(all_bags):
    bags_containing_sgb = []
    for i in range(len(all_bags)):
        for outer_bag in all_bags:
            if outer_bag not in bags_containing_sgb:
                for inner_bag in all_bags[outer_bag]:
                    if inner_bag == 'shiny gold' or inner_bag in bags_containing_sgb:
                        if outer_bag not in bags_containing_sgb:
                            bags_containing_sgb.append(outer_bag)
    print(len(bags_containing_sgb), 'bag colors contain at least one shiny gold bag')


def count_bags_in_bag(all_bags, searched_bag):
    count = 0
    inner_bags = all_bags[searched_bag]
    for inner_bag in inner_bags:
        if inner_bag == 'other':
            return 1
        else:
            count += int(inner_bags[inner_bag]) * count_bags_in_bag(all_bags, inner_bag)
    return count + 1


def main():
    all_bags = make_data()
    bags_with_searched_inner_bag(all_bags)
    print(count_bags_in_bag(all_bags, 'shiny gold') - 1, 'bags are required in the single shiny gold bag')


if __name__ == '__main__':
    main()
