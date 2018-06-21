from MenuConstuctor import *
from Wallet import *
from Calendar_for_wallet import *
from History import *


class Budget(Menu):
    def __init__(self, name=None, salary=0, day_of_salary='1900.01.01'):
        self.name = name
        self.wallet = Wallet(salary)
        self.calendar = Calendar(day_of_salary)
        self.history = History(self.wallet)



    def show_all_info(self):
        print('_'*10, 'Общая информация', '_'*10,'\n')
        print('День зарплаты: ' + str(self.calendar.get_day_of_salary()))
        self.calendar.show_date()
        self.calendar.count_days_before_salary()
        print('Общее: ', self.wallet.common)
        print('Развлечения: ', self.wallet.fun)
        print('Инвестиции: ', self.wallet.invest)
        print('Budget ', self.wallet._salary)

        print('Сегодня вы моgете потратить из обшего бюдета: ', self.wallet.show_max_50_for_today(self.calendar.counter_days))
        print('Сегодня вы моgете потратить на развлечения:', self.wallet.show_max_30_for_today(self.calendar.counter_days))

        print('История:')
        self.history.get_trans()
        print('Бюдget: ', self.history.get_budget())

    def expenses(self,expenses):

        mnu = {
            '1': self.wallet.common_50_minus,
            '2': self.wallet.fun_30_minus,
            '3': self.wallet.invest_20_minus,
            '4': self.wallet.minus_salary
        }
        self.show_mnu(mnu, ['из 50', 'из 30', 'из 20', 'From budget'], 'Расxоды')

        n = input()

        res = mnu.get(n)(expenses)


        # add to history
        if int(n) == 4:
            self.history.budget_changed(res)
            self.history.transaction(self.calendar.show_clean_date(), '-budget:' + str(expenses))
        elif int(n) < 4 and int(n) >= 1:
            self.history.transaction(self.calendar.show_clean_date(), res)
        else:
            print('Error menu item')

    def add_in_budget(self, salary):

        mnu = {
            '1': self.wallet.common_50_add,
            '2': self.wallet.fun_30_add,
            '3': self.wallet.invest_20_add,
            '4': self.wallet.add_salary
        }

        self.show_mnu(mnu, ['в 50', 'в 30', 'в 20', 'Into budget'], 'Add')

        n = input()

        try:
            res = mnu.get(n)(salary)
        except Exception:
            return 'errror in menu item'

        # add to history
        if n == '4':
            self.history.budget_changed(res)
            self.history.transaction(self.calendar.show_clean_date(), '+budget:' + str(salary))
        else:
            self.history.transaction(self.calendar.show_clean_date(), res)


if __name__ == '__main__':

    arcan = Budget(15000, '2018.06.08')
    arcan.show_all_info()
    # arcan.expenses(103)
    # arcan.show_all_info()
    # arcan.add_in_budget(19000)
    # arcan.show_all_info()
    # arcan.show_all_info()

    # arcan.add_in_budget(770)
    # arcan.show_all_info()
    #
    # arcan.add_in_budget(1500)
    # arcan.show_all_info()
    # arcan.expenses(1000)
    #
    # arcan.show_all_info()

    arcan.expenses(1000)
    arcan.show_all_info()
    arcan.expenses(1000)
    arcan.show_all_info()

    arcan.add_in_budget(100)
    arcan.show_all_info()