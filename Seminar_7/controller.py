import logic
import const
import logger
import view


def button_click():
    menu_choise = -2
    type_choise = const.VALUE[0]
    last_result = None
    while menu_choise != const.MENU[-1]:
        menu_choise = view.print_menu()
        if menu_choise == const.MENU[1]:
            type_choise = view.choose_value()
        elif menu_choise == const.MENU[2]:
            print(f'Операции проходят с типом данных: {type_choise}')
            a = view.input_arguements(type_choise)
            b = view.input_arguements(type_choise)
            operation = view.operation()
            last_result = view.oper_result(a, b, operation)
            print (f'{a} {const.OPERATION[operation]} {b} = {last_result}')
        elif menu_choise == const.MENU[0]:
            if last_result:
                a = last_result
                b = view.input_arguements(type_choise)
                last_result = view.oper_result(a, b, operation)
            else:
                print ('Вычисления еще не производились. Выберите другой пункт меню.')
        elif menu_choise == const.MENU[3]:
            logger.view_log()
        elif menu_choise == const.MENU[4]:
            exit('Завешение работы')