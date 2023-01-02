from datetime import datetime as dt
import csv

# Добавляет записи в лог

def write_in_log(data):
    time =  dt.now().strftime('%H:%M, %d. %m. %Y.')
    with open ('Homeworks/Seminar_7/log.csv','a') as log_file:
        log_file.writelines(f'{time} - {data}')

# Выводит записи из лога в терминал

def view_log():
    with open('Homeworks/Seminar_7/log.csv', 'r', newline='') as lg:
        log_reader = csv.reader(lg)
        for line in log_reader:
            print(f'{line}\n')