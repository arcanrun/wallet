from b import *
import shelve
import sys

if __name__ == '__main__':

    def exit():
        print('Exit: y / n?')
        ans = input()
        if ans == 'y':
            db[wallet.name] = wallet
            db.close()
            sys.exit('Bye-bye!')
        else:
            mainMenu()


    db = shelve.open('wallet-db')

    wallet = Budget()
    menu = Menu()


    print('From histoty: ', wallet.history.get_budget())

    if len(db) == 0:
        print('Введите имя владельца кошелька')
        name = input()

        print('Введите сумму зарплаты')
        zarp = input()

        print('Введите когда вы получили зарплату: год.месяц.день')
        day = input()


        wallet = Budget(name, zarp, day)
        db[wallet.name] = wallet
        wallet = db[wallet.name]
        wallet.show_all_info()
    else:
        print('Пользователи:')
        i = 1
        for k, v in db.items():
            print('\t',i,'.',k)
            i += 1
        i = 1

    mnu = {
        '1': wallet.expenses,
        '2': wallet.add_in_budget,
        '3': wallet.calendar.set_next_day_salary,
        '4': wallet.calendar.set_day_of_salary,
        '5': wallet.show_all_info,
        '6': wallet.history.get_trans,
        '7': exit
    }

    mnu_items = [
        'Расxоды',
        'Доxоды',
        'Изменить день зарплаты для следующей зарплты',
        'Изменить день текущей зарплаты',
        'Вся информация',
        'История',
        'Выход'

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
        db[wallet.name] = wallet
# ======== here we go =========
    mainMenu()


