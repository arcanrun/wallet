class Wallet:
    def __init__(self, new_salary):
        self._salary = float(new_salary)
        self.common_fun_invest()

    def set_salary(self, new_salary):
        self._salary = new_salary

    def get_salary(self):
        print(self._salary)

    def get_clean_salary(self):
        return self._salary

    def common_fun_invest(self):
        self.common = round(self._salary * 0.5)
        self.fun = round(self._salary * 0.3)
        self.invest = round(self._salary * 0.2)

    def minus_salary(self, expenses):
        expenses = float(expenses)
        self._salary -= expenses
        self.common_fun_invest()

        return self._salary


    def show_budget(self):
        print('\nYour budget: ' + str(self.salary))

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
        self.common -= expenses
        self._salary -= expenses

        return '-common:' + str(expenses)

    def fun_30_minus(self, expenses):
        expenses = float(expenses)
        self.fun -= expenses
        self._salary -= expenses

        return '-fun:' + str(expenses)

    def invest_20_minus(self, expenses):
        expenses = float(expenses)
        self.invest -= expenses
        self._salary -= expenses

        return '-invest:' + str(expenses)

    def add_salary(self, salary):
        salary = float(salary)
        self._salary += salary
        self.common_fun_invest()

        return self._salary

    def show_max_50_for_today(self, days):
        return self.common / days

    def show_max_30_for_today(self, days):
        return self.fun / days







