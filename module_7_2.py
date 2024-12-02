def custom_write(file_name, *strings):
    strings_for_write = list(*strings)
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(len(strings_for_write)):
        bite = file.tell()
        strings_positions[i + 1, bite] = strings_for_write[i]
        file.write(f'{strings_for_write[i]}\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)