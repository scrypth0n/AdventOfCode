def make_data():
    with open('09_input') as file:
        nums = file.readlines()
    numbers = []
    for num in nums:
        numbers.append(int(num.replace('\n', '')))
    return numbers


def find_encoding_error(nums, k=0):
    check = False
    for i in range(k, 25 + k):
        for j in range(k, 25 + k):
            if nums[i] + nums[j] == nums[25 + k]:
                check = True
    if check:
        return find_encoding_error(nums, k + 1)
    else:
        return [nums[25 + k], k]


def find_weakness(nums, num):
    count_nums_for_addition = 1
    while True:
        count_nums_for_addition += 1
        for i in range(num[1] - 1 - count_nums_for_addition):
            value_ports = 0
            for j in range(count_nums_for_addition):
                value_ports += nums[i + j]
            if value_ports == num[0]:
                list_ports = []
                for j in range(count_nums_for_addition):
                    list_ports.append(nums[i + j])
                return min(list_ports) + max(list_ports)


def main():
    data = make_data()
    num = find_encoding_error(data)   #[number, location]
    print('Encoding error:', num[0])
    print('Encryption weakness', find_weakness(data, num))


if __name__ == '__main__':
    main()
