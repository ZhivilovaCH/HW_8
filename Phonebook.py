print('''Главное меню:
 1. Открыть файл
 2. Сохранить файл
 3. Показать все контакты
 4. Создать контакт
 5. Изменить контакт
 6. Найти контакт
 7. Удалить контакт
 8. Выход''')


phone_book = []
path = 'file.txt'

def open_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            cont = []
            for field in contact.split(';'):
                cont.append(field.strip())
            phone_book.append(cont)
print()
number = 2

def save_patch(path, phone_book):
    with open(path, 'w', encoding='UTF-8') as file:
        for contact in phone_book:
            cont = []
            for field in contact:
                # cont.append(field + ';')
                file.write(field + ';')
            file.write('\n')

def show_contacts(phone_book):
    for i, contact in enumerate(phone_book, 1):
        print(f'{i}. {contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')

def add_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    phone_book.append(list([name, phone, comment]))

def search_contact(phone_book):
    search = input('Введите ключевой элемент поиска: ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(contact)

def upd_contact(phone_book):
    search = input('Введите ключевой элемент : ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(f'{contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')
                contact[0] = input('Введите имя и фамилию: ')
                contact[1] = input('Введите телефон: ')
                contact[2] = input('Введите комментарий: ')

def del_contact(phone_book):
    search = input('Введите ключевой элемент для удаления: ')
    for contact in phone_book:
        for field in contact:
            if search in field:
                print(f'{contact[0]:<20}{contact[1]:<20}{contact[2]:<15}')
                phone_book.remove(contact)

while True:

    number = int(input('Введите пункт меню: '))

    match number:
        case 1:
            open_file(path)
            print('Файл успешно загружен')
        case 2:
            save_patch(path, phone_book)
            print('Файл сохранён')
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            upd_contact(phone_book)
        case 6:
            search_contact(phone_book)

        case 7:
            del_contact(phone_book)
            print(f'Контакт удалён')
        case 8:
            break













# print(' 1. Открыть файл\n 2. Сохранить файл\n 3. Показать все контакты\n 4. Создать контакт\n 5. Изменить контакт\n 6. Найти контакт\n 7. Удалить контакт\n 8. Выход')



