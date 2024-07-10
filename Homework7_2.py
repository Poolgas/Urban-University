

def custom_write(file_name: str, strings: list):
    file = open(file_name, 'w', encoding='utf-8')
    strings_position = dict()
    for i in range(len(strings)):
        strings_position[i + 1, file.tell()] = strings[i]
        file.write(f'{strings[i]}\r\n')
    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

