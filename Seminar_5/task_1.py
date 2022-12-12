# Напишите программу, удаляющую из текста все слова, содержащие заданную строку.


def removeChar(text, deleteWord):
    words = text.split(" ")
    words = [word for word in words if not deleteWord in word]
    answer = " ".join(words)
    return answer

text = input('Введите первоначальный текст:\n')
text.upper()
word = input('Введите слово, которое хотите удалить:\n')
word.upper()
result = removeChar(text, word)
print(result.lower())