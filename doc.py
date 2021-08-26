documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

commands = [
    'p - определение имени человека по номеру документа',
    's - определение номера полки по номеру документа',
    'l - список всех документов',
    'a - добавление нового документа в каталог и в перечень полок'
]
print('Доступные команды:')
for el in commands:
    print(f'{el}')

def data_person(input_number):
    search_name = False
    for person in documents:
        for number in person.values():
            if number == input_number:
                search_name = person['name']
    return search_name

def data_shelf(input_number):
    search_shelf = False
    for key, value in directories.items():
        for number in value:
            if number == input_number:
                search_shelf = key
    return search_shelf

def data_print():
    for person in documents:
        list_value = []
        for value in person.values():
            list_value.append(value)
        print(' '.join(list_value))
    return

def add_data():
    doc_type = input('Введите тип документа: ')
    doc_number = input('Введите номер документа: ')
    doc_name = input('Введите Ваше имя: ')
    doc_shelf = input('Введите номер полки: ')
    add_dict = {"type": doc_type, "number": doc_number, "name": doc_name}
    documents.append(add_dict)
    print('Ваши документы успешно добавлены. Вы можете проверить результат с помощью команды "l"')
    if doc_shelf in directories.keys():
        for key, value in directories.items():
            if key == doc_shelf:
                value.append(doc_number)
        print(f'Ваши документы успешно размещены на полке №{doc_shelf}.')
    else:
        print('Такой полки не существует!')
    return

# while True:
#     user_input = input('Введите команду: ')
#     if user_input == 'p':
#         input_number = input('Введите номер документа: ')
#         if data_person(input_number):
#             print(data_person(input_number))
#         else:
#             print('Введенный Вами номер отсутствует в базе данных!')
#     elif user_input == 's':
#         input_number = input('Введите номер документа: ')
#         if data_shelf(input_number):
#             print(f'Ваш документ находится на полке №{data_shelf()}.')
#         else:
#             print('Введенный Вами номер отсутствует в базе данных!')
#     elif user_input == 'l':
#         print(data_print())
#     elif user_input == 'a':
#         add_data()
#     elif user_input == 'q':
#         print('До свидания!')
#         break
#     else:
#         print('Такой команды нет')