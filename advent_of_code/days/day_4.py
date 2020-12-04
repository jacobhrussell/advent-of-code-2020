import csv

# https://adventofcode.com/2020/day/4

def main():
    my_input = []
    with open('advent_of_code/input/day_4.csv', newline='') as inputfile:
        passport = {}
        for row in csv.reader(inputfile):
            if len(row) > 0:
                key_vals = row[0].split(" ")
                for key_val in key_vals:
                    key, val = key_val.split(":")
                    passport[key] = val
            else:
                my_input.append(passport)
                passport = {}
        my_input.append(passport)

    number_of_valid_passports = check_valid_passports(my_input)
    print("Number of valid passports: {}".format(number_of_valid_passports))

    number_of_valid_passports = check_valid_passports_part_2(my_input)
    print("Number of valid passports for part 2: {}".format(number_of_valid_passports))

def check_valid_passports(passports):
    number_of_valid_passports = 0
    for passport in passports:
        if "cid" in passport:
            if len(passport) == 8:
                number_of_valid_passports = number_of_valid_passports + 1
        else:
            if len(passport) == 7:
                number_of_valid_passports = number_of_valid_passports + 1
    return number_of_valid_passports

def check_valid_passports_part_2(passports):
    number_of_valid_passports = 0
    for passport in passports:
        valid = True
        if ("cid" in passport and len(passport) == 8) or ("cid" not in passport and len(passport) == 7):
            if len(passport["byr"]) != 4 or int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
                valid = False
            if len(passport["iyr"]) != 4 or int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
                valid = False
            if len(passport["eyr"]) != 4 or int(passport["eyr"]) < 2020 or int(passport["eyr"]) > 2030:
                valid = False
            if not try_cast(passport["hgt"][:len(passport["hgt"])-2], int) or not check_height_value(passport["hgt"]):
                valid = False
            if passport["ecl"] != "amb" and passport["ecl"] != "blu" and passport["ecl"] != "brn" and passport["ecl"] != "gry" and passport["ecl"] != "grn" and passport["ecl"] != "hzl" and passport["ecl"] != "oth":
                valid = False
            if not try_cast(passport["pid"], int) or len(passport["pid"]) != 9:
                valid = False
            if not check_hair_color(passport["hcl"]):
                valid = False
        else:
            valid = False
        if valid:
                number_of_valid_passports = number_of_valid_passports + 1
    return number_of_valid_passports

def try_cast(val, to_type):
    try:
        my_val = to_type(val)
        return True
    except (ValueError, TypeError):
        return False

def check_height_value(height):
    valid = True
    height_value = int(height[:len(height)-2])
    if height[-2:] != "cm" and height[-2:] != "in":
        valid = False
    if height[-2:] == "cm":
        if height_value < 150 or height_value > 193:
            valid = False
    if height[-2:] == "in":
        if height_value < 59 or height_value > 76:
            valid = False
    return valid

def check_hair_color(hair_color):

    valid = True

    ok_characters = "0123456789abcdef"

    if hair_color[:1] != "#":
        valid = False

    if len(hair_color[1:]) != 6:
        valid = False

    if not all(c in ok_characters for c in hair_color[1:]):
        valid = False
    
    return valid

if __name__ == "__main__":
    main()