def make_data():
    with open('09_input') as file:
        nums = file.readlines()
    numbers = []
    for num in nums:
        numbers.append(int(num.replace('\n', '')))
    return numbers


def a(nums, k=0):
    check = False
    for i in range(k, 25 + k):
        for j in range(k, 25 + k):
            if nums[i] + nums[j] == nums[25 + k]:
                check = True
    if check:
        return a(nums, k + 1)
    else:
        return [nums[25 + k], k]


def b(nums, num):
    check = False
    value = 0
    for i in range(num[1], 25 + num[1]):
        for j in range(num[1], 25 + num[1]):
            for k in range(num[1], 25 + num[1]):
                for l in range(num[1], 25 + num[1]):
                    if nums[i] + nums[j] + nums[k] + nums[l] == num[0]:
                        liste = (nums[i], nums[j], nums[k], nums[l])
                        return min(liste) + max(liste)


def main():
    data = make_data()
    ab = a(data)
    print('01:', ab[0])
    print('02:', b(data, ab))


if __name__ == '__main__':
    main()
