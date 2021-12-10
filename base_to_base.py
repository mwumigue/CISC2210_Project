import math

digits = "0 1 2 3 4 5 6 7 8 9 A B C D E F"
output = []


def decimal_to_other_base(number, n, list):
    if number != 0 and n == 0:
        return None

    remainder = number % n

    if number < 1:
        return "".join(list)

    elif n == 1:
        list.append(digits.split()[1])
        return decimal_to_other_base(number - 1, n, list)

    list.insert(0, digits.split()[remainder])
    return decimal_to_other_base(number // n, n, list)


def other_base_to_decimal(number, base):
    total = 0
    base_digits = []
    for i in range(base):
        base_digits.append(digits.split()[i])

    for j in number:
        if j not in base_digits:
            return None

    for k in range(len(number)-1, -1, -1):
        for l in range(len(base_digits)):
            if number[k] == base_digits[l]:
                total = total + (l * math.pow(base, len(number) - (k + 1)))

    return int(total)


def base_to_base(number, from_base, to_base):
    new_output = []
    if from_base == 10:
        return decimal_to_other_base(int(number), to_base, new_output)

    elif to_base == 10:
        return other_base_to_decimal(number, from_base)

    elif from_base == to_base:
        return number

    else:
        temp_number = other_base_to_decimal(number, from_base)
        if temp_number is None:
            return temp_number
        return decimal_to_other_base(temp_number, to_base, new_output)


def user_prompt():
    number = str(input("Enter the number you want to translate: "))
    from_base = int(input("Enter the number base you want to translate from (1-16): "))
    to_base = int(input("Enter the number base you want to translate to (1-16): "))
    print(base_to_base(number, from_base, to_base))
    continuation = str(input("Do you wish to continue? (y/n) "))
    if continuation == "n" or continuation == "N":
        print("Process ended")
    else:
        user_prompt()


print(user_prompt())
