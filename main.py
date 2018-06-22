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

    def clear_db():
        print('Удалить все данные?\nY / N:')
        res = input()
        if res == 'Y' or res == 'y':
            print('Вы уверены? 3то удалит все накопленные данные!\nY / N:')
            res_2 = input()
            if res_2 == 'Y' or res_2 == 'y':
                db.clear()
                sys.exit('Базаданныx очищена!')
            else:
                mainMenu()
        else:
            mainMenu()

    def create_user():
        print('Введите имя владельца кошелька')
        name = input()

        print('Введите сумму зарплаты')
        zarp = input()

        print('Введите когда вы получили зарплату: год.месяц.день')
        day = input()

        wallet = Budget(name, zarp, day)

        return wallet

    db = shelve.open('wallet-db')

    wallet = Budget()
    menu = Menu()


    print('From histoty: ', wallet.history.get_budget())

    if len(db) == 0:
        wallet = create_user()
        db[wallet.name] = wallet
        wallet = db[wallet.name]

        wallet.show_all_info()

    else:
        print('Пользователи:')
        i = 1
        users = []
        for k, v in db.items():
            print('\t',i,'.',k)
            users.append(k)
            i += 1
        i = 1
        print('Выберите пользователя:')
        user = int(input())-1
        try:
            wallet = db[users[user]]
            print('Пользователь под именем', wallet.name, 'выбран')
        except Exception:
            sys.exit('\tERROR!: Такого пользователя не существует!')


    mnu = {
        '1': wallet.expenses,
        '2': wallet.add_in_budget,
        '3': wallet.calendar.set_next_day_salary,
        '4': wallet.calendar.set_day_of_salary,
        '5': wallet.show_all_info,
        '6': wallet.history.get_trans,
        '7': None,
        '8': exit,
        '9': clear_db
    }

    mnu_items = [
        'Расxоды',
        'Доxоды',
        'Изменить день зарплаты для следующей зарплты',
        'Изменить день текущей зарплаты',
        'Вся информация',
        'История',
        'Новый пользователь',
        'Сохранить и выйти',
        'Очистить базу данныx'

    ]

    def mainMenu():
        menu.show_mnu(mnu, mnu_items)
        n = input()

        if n.isalpha() or (int(n) < 1 or int(n) == 5 or int(n) == 6 or int(n) >= 8):
            mnu.get(n, mainMenu)()
            mainMenu()
        elif int(n) == 7:
            wallet = create_user()
            db[wallet.name] = wallet
            wallet = db[wallet.name]

            wallet.show_all_info()
            mainMenu()

        else:
            print('Значение:')
            m = input()
            mnu.get(n, mainMenu)(m)
            mainMenu()




# ======== here we go =========
    mainMenu()


