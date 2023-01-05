from interface import get_menu_item
from delete_cont import delete_contact
from add_cont import add_contact
from finder import search_by
from show_db import show


def procedure():
    while True:
        choice = get_menu_item()
        if choice == 1:
            add_contact()
        elif choice == 2:
            delete_contact()
        elif choice == 4:
            search_by()
        elif choice == 5:
            show()
        elif choice == 6:
            exit()