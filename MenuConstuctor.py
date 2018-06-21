class Menu:

    def show_mnu(self, menu, list_title=[], menu_title='Menu'):

        print('_'*10, menu_title, '_'*10, '\n')


        i = 0 # for titles
        if len(list_title) == len(menu):
            for k,v in menu.items():
                print('|',k, list_title[i])
                i += 1
        else:
            print("Cant't make menu:\n\t Error in title list and valuses of menu")

        print('_'*20)