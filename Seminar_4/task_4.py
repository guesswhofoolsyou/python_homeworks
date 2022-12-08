# Шифр Цезаря
# Написать функцию, которая записывает в файл шифрованный текст,
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

alfavit_RUS = ' ,.АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_ENG = ' ,.ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lang = int(input('Выбирете язык\n1 - RUS\n2 - ENG:\n'))
text = input('Введите текст послания:\n').upper()
password = int(input('Введите значение смещения символов: '))
new_text = ''

for i in text:
    if lang == 1:
        value = alfavit_RUS.find(i)
        if value >= 0 and value <= 2:
            new_value = value
        else:
            new_value = value + password
        if i in alfavit_RUS and new_value < len(alfavit_RUS):
            new_text += alfavit_RUS[new_value]
        else:
            new_text += alfavit_RUS[3+(new_value-len(alfavit_RUS))]
    elif lang == 2:
        value = alfavit_ENG.find(i)
        if value >= 0 and value <= 2:
            new_value = value
        else:
            new_value = value + password
        if i in alfavit_ENG and new_value < len(alfavit_ENG):
            new_text += alfavit_ENG[new_value]
        else:
            new_text += alfavit_ENG[3+(new_value-len(alfavit_ENG))]
    else:
        print ('Неизвестный язык')

new_text = new_text.lower()


data = open('Homeworks/Seminar_4/encryption.txt','w')
data.writelines(new_text)
data.close()

print('\n\n\n')

decrypt = open('Homeworks/Seminar_4/encryption.txt','r')
read_text = decrypt.read()
read_text = read_text.upper()
decr_text = ''
print (read_text)
lang = int(input('Выберите язык\n1 - RUS\n2 - ENG:\n'))
decr_password = int(input('Введите значение смещения символов: '))

for i in read_text:
    if lang == 1:
        value = alfavit_RUS.find(i)
        if value >= 0 and value <= 2:
            new_value = value
        elif value - decr_password > 2:
            new_value = value - decr_password
        else:
            new_value = value + len(alfavit_RUS) - decr_password - 3
        decr_text += alfavit_RUS[new_value]
    elif lang == 2:
        value = alfavit_ENG.find(i)
        if value >= 0 and value <= 2:
            new_value = value
        elif value - decr_password > 2:
            new_value = value - decr_password
        else:
            new_value = value + len(alfavit_ENG) - decr_password - 3
        decr_text += alfavit_ENG[new_value]

    else:
        print ('Неизвестный язык')

decr_text = decr_text.lower()
print (decr_text)
