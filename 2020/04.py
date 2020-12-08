import re


def split_data(line_, dictionary):
    data = line_.split(' ')
    for d in data:
        d = d.split(':')
        dictionary[d[0]] = d[1].replace('\n', '')
    return dictionary


def main():
    with open("04_input") as file:
        file = list(file.readlines())
    passports = []
    new_passport = True
    passport = {}
    for line in file:
        if line == '\n':
            new_passport = True
            passports.append(passport)
        elif new_passport:
            new_passport = False
            passport = split_data(line, {})
        else:
            passport = split_data(line, passport)
    passports.append(passport)
    valid1 = 0
    valid2 = 0
    for passport in passports:
        if (passport.__contains__('byr') and passport.__contains__('iyr') and passport.__contains__('eyr') and
                passport.__contains__('hgt') and passport.__contains__('hcl') and passport.__contains__('ecl') and
                passport.__contains__('pid')):
            valid1 += 1
            if 'cm' in passport['hgt']:
                hgt_valid = 150 <= int(passport['hgt'].replace('cm', '')) <= 193
            elif 'in' in passport['hgt']:
                hgt_valid = 59 <= int(passport['hgt'].replace('in', '')) <= 76
            else:
                hgt_valid = False
            if (1920 <= int(passport['byr']) <= 2002 and re.match(r"^#[a-f0-9]{6}$", passport['hcl']) and
                    2010 <= int(passport['iyr']) <= 2020 <= int(passport['eyr']) <= 2030 and hgt_valid and
                    passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and
                    re.match(r"^[0-9]{9}$", passport['pid'])):
                valid2 += 1
    print('Valid Passports: 1', valid1)
    print('Valid Passports: 2', valid2)


if __name__ == "__main__":
    main()
