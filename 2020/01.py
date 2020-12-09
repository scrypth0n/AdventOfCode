with open("01_input") as file:
    nums = list(map(int, file.readlines()))

for i in nums:
    for j in nums:
        if i + j == 2020:
            solution2 = i * j
        for k in nums:
            if i + j + k == 2020:
                solution3 = i * j * k

print('Solution 2 numbers: ', solution2)
print('Solution 3 numbers: ', solution3)
