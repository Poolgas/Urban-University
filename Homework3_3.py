def get_multipllied_digits(number):
    str_numbers = str(number)
    first = int(str_numbers[0])
    if len(str_numbers) <= 1:
        return first
    return first * get_multipllied_digits(int(str_numbers[1:]))

print(get_multipllied_digits(40203))