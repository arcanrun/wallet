import datetime

class Calendar:
    def __init__(self, day_of_salary):

        self._day_of_salary = datetime.datetime(int(day_of_salary.split('.')[0]),
                                               int(day_of_salary.split('.')[1]),
                                               int(day_of_salary.split('.')[2]))
        self._next_payday = datetime.datetime(self._day_of_salary.year, self._day_of_salary.month + 1,
                                             self._day_of_salary.day)

    def get_day_of_salary(self):
        return self._day_of_salary.strftime('%d-%m-%Y')

    def set_day_of_salary(self, new_day_of_salary):
        self._day_of_salary = datetime.datetime(int(new_day_of_salary.split('.')[0]),
                                               int(new_day_of_salary.split('.')[1]),
                                               int(new_day_of_salary.split('.')[2]))

    def get_next_day_salary(self):
        return self._next_payday

    def set_next_day_salary(self, new_next_day_salary):
        self._next_payday = datetime.datetime(int(new_next_day_salary.split('.')[0]),
                                              int(new_next_day_salary.split('.')[1]),
                                              int(new_next_day_salary.split('.')[2]))

    def show_date(self):
        print('Сегодня: ', datetime.date.today().strftime('%d-%m-%Y'))

    def show_clean_date(self):
        return str(datetime.date.today().strftime('%d-%m-%Y'))

    def count_days_before_salary(self):
        self.counter_days = (self._next_payday - datetime.datetime.now()).days
        if int(self.counter_days +1) == 0:
            self.day_of_salary = datetime.datetime.now()
            self._next_payday = datetime.datetime(self.day_of_salary.year, self.day_of_salary.month + 1,
                                                 self.day_of_salary.day)
            self.counter_days = (self._next_payday - datetime.datetime.now()).days
        print('До следующей зарплаты осталось:', self.counter_days + 1,'дня:', self._next_payday.strftime('%d-%m-%Y'))
