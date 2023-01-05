from func import give_int
from const import func

choose_option = 'Выберите действие из списка:\n'


def get_menu_item() -> int:
    for i, item in list(enumerate(func, start=1)):
        print(i, item, end='\n')
    choice = give_int(choose_option, 1, 7)
    return choice


if __name__ == '__main__':
    choice = get_menu_item()