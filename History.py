class History:
    """Save to the DB

        Example:

            trans_from_ = {
                10_04_2018:['-fun:150', '+common:76'],
                11_04_2018:['-common:73'],
                12_04_2018:['+budget:1000']
            }
    """
    def __init__(self):
        self.trans = {}

    def get_trans(self):
        if len(self.trans) == 0:
            print('**** В истории нет записей ****')
        else:
            for k,v in self.trans.items():
                print(k,':')
                for i in v:
                    print('\t',i)

    def transaction(self, date, trans_val):
        if date in self.trans:
            self.trans[date].append(trans_val)
        else:
            self.trans[date] = [trans_val]
