from collections import Counter

def is_valid_password(password):
    password_list = [int(d) for d in str(password)]
    return is_six_digits(password_list) and has_two_adjacent_digits(password_list) and digits_never_decrease(password_list)

def is_six_digits(password_list):
    return len(password_list) == 6

def has_two_adjacent_digits(password_list):
    counter = Counter(password_list)
    multiple_digits = {k:v for k,v in counter.items() if int(v) > 1}
    for digit in multiple_digits:
        # get all of the indices with digit
        indices = [i for i, x in enumerate(password_list) if x == digit]
        for index in indices:
            this_digit = password_list[index]
            if index < 5: # make sure it isn't the last digit
                next_digit = password_list[index + 1]
                if this_digit == next_digit:
                    return True
    return False

def digits_never_decrease(password_list):
    last_digit = -1
    for digit in password_list:
        digit_int = int(digit)
        if last_digit > digit_int:
            return False
        else:
            last_digit = digit_int
    return True

def calc_num_passwords(lower_bound, upper_bound):
    # this could be made much faster by not checking passwords we know are invalid,
    # but for now we'll brute force
    valid_passwords = map(is_valid_password, range(lower_bound, upper_bound))
    valid_password_count = Counter(valid_passwords)
    return valid_password_count.get(True)

assert has_two_adjacent_digits(['1', '2', '2', '3', '4', '5']) == True
assert has_two_adjacent_digits(['1', '2', '3', '4', '5', '6']) == False

assert digits_never_decrease(['2', '2', '3', '4', '5', '0']) == False
assert digits_never_decrease(['1', '2', '3', '4', '5', '6']) == True

print(calc_num_passwords(128392, 643281))