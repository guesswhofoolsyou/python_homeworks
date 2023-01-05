from func import get_lines, write_lines
from const import data, contacts_temps
from finder import search_by


def delete_contact():
    reader = get_lines()
    choice = search_by()
    try:
        reader.remove(choice[0])
    except IndexError:
        return print("Couldn't find data")
    reader.insert(0, contacts_temps.keys())
    write_lines(data, reader)
    return print("Removing comlete")