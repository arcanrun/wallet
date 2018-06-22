class Wallet:
    def __init__(self, new_salary):
        self._salary = float(new_salary)
        self.common_fun_invest()

    def set_salary(self, new_salary):
        self._salary = new_salary

    def get_salary(self):
        return round(self._salary, 2)

    salary = property(get_salary, set_salary, None, None)

    def get_clean_salary(self):
        return round(self._salary - self.invest, 2)

    def get_invest(self):
        return self.invest

    def common_fun_invest(self):
        self.common = round(self._salary * 0.5, 2)
        self.fun = round(self._salary * 0.3, 2)
        self.invest = round(self._salary * 0.2, 2)

    def minus_salary(self, expenses):
        expenses = float(expenses)
        expenses = float(expenses)
        if expenses > self._salary:
            return 'error'
        else:
            self._salary -= expenses
            return '-budget:' + str(expenses)

    def common_50_add(self,salary):
        salary = float(salary)
        self.common += salary
        self._salary += salary

        return '+common:' + str(salary)

    def fun_30_add(self, salary):
        salary = float(salary)
        self.fun += salary
        self._salary += salary

        return '+fun:' + str(salary)

    def invest_20_add(self, salary):
        salary = float(salary)
        self.invest += salary
        self._salary += salary

        return '+invest:' + str(salary)

    def common_50_minus(self, expenses):
        expenses = float(expenses)
        if expenses > self.common:
            return 'error'
        else:
            self.common -= expenses
            self._salary -= expenses

            return '-common:' + str(expenses)

    def fun_30_minus(self, expenses):
        expenses = float(expenses)
        expenses = float(expenses)
        if expenses > self.fun:
            return 'error'
        else:
            self.fun -= expenses
            self._salary -= expenses

            return '-fun:' + str(expenses)

    def invest_20_minus(self, expenses):
        expenses = float(expenses)
        expenses = float(expenses)
        if expenses > self.invest:
            return 'error'
        else:
            self.invest -= expenses
            self._salary -= expenses

            return '-invest:' + str(expenses)

    def add_salary(self, salary):
        salary = float(salary)
        self._salary += salary
        self.common_fun_invest()

        return '+budget:' + str(salary)

    def show_max_50_for_today(self, days):
        return round(self.common / days, 2)

    def show_max_30_for_today(self, days):
        return round(self.fun / days, 2)

    def show_budget(self):
        print('\nYour budget: ' + str(self.salary))







