#  В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов,
# которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

names = \
    ['John Snow 5\n',
    'James Brown 5\n',
    'Kanye West 3\n',
    'Steffan Carry 4\n',
    'Leo Messi 3']

data = open('Homeworks/Seminar_4/students_list.txt','w')
data.writelines(names)
names.insert(0,'\n\n')
for line in names:
    data.writelines(line.upper())
