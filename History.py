class History:
    """Save to the DB

        Example:

            trans_from_ = {
                10_04_2018:['-fun:150', '+common:76'],
                11_04_2018:['-common:73'],
                12_04_2018:['+budget:1000']
            }
    """
    def __init__(self, budget = None):
        self.budget = budget
        self.trans = {}
    def get_trans(self):

        for k,v in self.trans.items():
            print(k,v)

    def transaction(self, date, trans_val):
        if date in self.trans:
            self.trans[date].append(trans_val)
        else:
            self.trans[date] = [trans_val]

    def budget_changed(self, budget):
        self.budget.set_salary = budget

    def get_budget(self):
        return self.budget.get_clean_salary()
