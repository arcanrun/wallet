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

        print('_'*10, 'Общая информация ', self.name , '_'*10,'\n')
        self.calendar.show_date()
        print('День зарплаты: ' + str(self.calendar.get_day_of_salary()))

        self.calendar.count_days_before_salary()
        print('.'*50)
        print('Общее: ', round(self.wallet.common,2))
        print('Развлечения: ', self.wallet.fun)
        print('Инвестиции: ', self.wallet.invest)
        print()

        print('Бюджeт: ', self.history.get_budget(), '/', 'Инвестиции: ', self.wallet.get_invest())
        print('Все деньги:  ', round(self.wallet._salary, 2))
        print('.'*50)


        print('Сегодня вы можете потратить из обшего бюджета: ', self.wallet.show_max_50_for_today(self.calendar.counter_days))
        print('Сегодня вы можете потратить на развлечения:', self.wallet.show_max_30_for_today(self.calendar.counter_days))
        print('.'*50)
        print('_'*20,'История:', '_'*20)

      


    def check_correct_expenses(self, result):
        if result == 'error':
            print('**** ERROR: расxоды больше существующей суммы! ****')
        else:
            if 'budget' in result:
                self.history.budget_changed(result)
            self.history.transaction(self.calendar.show_clean_date(), result)

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

        if int(n) < int(len(mnu)) or int(n) > 1:
            self.check_correct_expenses(res)
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