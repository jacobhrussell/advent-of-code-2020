import csv

# https://adventofcode.com/2020/day/2
def main():
    my_input = []
    with open('advent_of_code/input/day_2.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            my_input.append(row[0])
    
    number_of_valid_passwords = 0
    for row in my_input:
        parts = get_parts(row)
        min_max = get_min_max(parts[0])
        letter = get_letter(parts[1])
        password = parts[2]
        is_valid = policy_1_check_is_valid(min_max, letter, password)
        if is_valid:
            number_of_valid_passwords = number_of_valid_passwords + 1
    print("Number of valid passwords for policy 1: {}".format(number_of_valid_passwords))

    number_of_valid_passwords = 0
    for row in my_input:
        parts = get_parts(row)
        min_max = get_min_max(parts[0])
        letter = get_letter(parts[1])
        password = parts[2]
        is_valid = policy_2_check_is_valid(min_max, letter, password)
        if is_valid:
            number_of_valid_passwords = number_of_valid_passwords + 1
    print("Number of valid passwords for policy 2: {}".format(number_of_valid_passwords))

def get_parts(line):
    parts = line.split(" ")
    return parts

def get_min_max(part):
    min_max = part.split("-")
    return min_max

def get_letter(part):
    letter = part.split(":")[0]
    return letter

def policy_1_check_is_valid(min_max, letter, password):
    minimum = int(min_max[0])
    maximum = int(min_max[1])
    number_of_occurances = 0
    for character in password:
        if character == letter:
            number_of_occurances = number_of_occurances + 1
    if number_of_occurances <= maximum and number_of_occurances >= minimum:
        return True
    else:
        return False

def policy_2_check_is_valid(min_max, letter, password):
    position_1 = int(min_max[0]) - 1
    position_2 = int(min_max[1]) - 1
    counter = 0
    if password[position_1] == letter:
        counter = counter + 1
    if password[position_2] == letter:
        counter = counter + 1
    if counter == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    main()