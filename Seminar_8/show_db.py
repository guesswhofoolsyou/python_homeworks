from func import get_lines


def show():
    reader = get_lines()
    for row in reader:
        print(*row)