def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list):
    count_calls()
    for i in list:
        a = 0
        if string.lower() in i.lower():
            a += 1
    if a > 0:
        return True
    else:
        return False

calls = 0


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)