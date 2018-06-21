from b import *


if __name__ == '__main__':

    arcan = Budget()
    menu = Menu()

    print('From histoty: ', arcan.history.get_budget())

    if arcan.history.get_budget() == 0:
        print('Введите сумму зарплаты')
        zarp = input()
        print('Введите когда вы получили зарплату: год.месяц.день')
        day = input()
        arcan = Budget(zarp, day)
    arcan.show_all_info()

    mnu = {
        '1': arcan.expenses,
        '2': arcan.add_in_budget,
        '3': arcan.calendar.set_next_day_salary,
        '4': arcan.calendar.set_day_of_salary,
        '5': arcan.show_all_info,
        '6': arcan.history.get_trans
    }

    mnu_items = [
        'Расxоды',
        'Доxоды',
        'Изменить день зарплаты для следующей зарплты',
        'Изменить день текущей зарплаты',
        'Вся информация',
        'История'
    ]

    def mainMenu():
        menu.show_mnu(mnu, mnu_items)
        n = input()

        if n.isalpha() or (int(n) > 6 or int(n) < 1) or int(n) == 5 or int(n) == 6:
            mnu.get(n, mainMenu)()
            mainMenu()
        else:
            print('Значение:')
            m = input()
            mnu.get(n, mainMenu)(m)
            mainMenu()


    mainMenu()


