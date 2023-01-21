def import_data():
    with open('phone_directory.txt', 'a') as file:
        id = input('Введите id контакта: ')
        name = input('Введите имя  контакта: ')
        surname = input('Введите фамилию контакта: ')
        number = input('Введите номер контакта: ')
        comment = input('Введите комментарий: ')
        file.write(f'{id}; {name}; {surname}; {number}; {comment}\n')
