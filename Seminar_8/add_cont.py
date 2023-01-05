from const import data as dt
import csv
import os.path

def fieldnames():
    if not os.path.exists(
            dt):  # проверка существует ли файл (если да, то последующий код  функции не запускается)
        with open(dt, 'a', newline='') as file:
            writer = csv.writer(file, dialect='excel', delimiter=';')
            writer.writerow(['Имя', 'Фамилия', 'Телефон', 'Группа', 'Комментарий'])
            file.close()


def check_name(text):
    while not text.isalpha() or text == '':
        text = input('Ошибка! Обязательное поле, принимаются только буквы, повторите ввод: \n')
    return text.title()


def check_phone(num):
    while num == '' or not num[1:].isdigit() or num[
        0] != '+':  # не вводил проверку на количество символов, т.к. может быть иностранный номер
        num = input('Ошибка! Обязательное поле, принимаются только "+" и цифры, повторите ввод: \n ')

    with open(dt, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for item in reader:
            while num in item['Телефон']:
                num = input(f'Этот номер телефона уже записан в справочнике, введите другой номер: \n ')
    return num


def add_contact():
    fieldnames()
    name = check_name(input('Введите имя контакта: \n '))
    last_name = check_name(input('Введите фамилию контакта: \n '))
    phone = check_phone(input('Введите телефон контакта(+ код страны телефон (без пробелов)):\n '))
    group = input('Введите группу контакта: \n ')
    comment = input('Введите комментарий контакта:\n ')
    new_contact = {'Имя': name, 'Фамилия': last_name, 'Телефон': phone, 'Группа': group, 'Комментарий': comment}

    with open(dt, mode='a', newline='') as csv_file:
        field_names = ['Имя', 'Фамилия', 'Телефон', 'Группа', 'Комментарий']

        writer = csv.DictWriter(csv_file, fieldnames=field_names, dialect='excel', restval='', delimiter=';')
        writer.writerow(new_contact)
        csv_file.close()