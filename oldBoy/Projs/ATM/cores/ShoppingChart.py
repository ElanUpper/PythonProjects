# author: elan

class goods():

    good_list = [];

    def __init__(self, name, category, price):
        self.good = {
            'name': name,
            'category': category,
            'price': price
        }
        goods.good_list.append(self.good)

    def delete_good(self, name):
        goods.good_list.pop(name);

    def change_good(self, name, category=None, price=0.0):
        index = 0
        for i in range(len(good_list)):
            if good_list[i].get('name') == name:
                index = i ;
                break
        if inex == 0 :
            print('{} not found'.format(name)) ;

        if None != category :
            lista[index]['category'] = category ;
        if 0.0 != price:
            lista[index]['price'] = price ;

class chart():

    def __init__(self):
        self.total_money = 10000;
        self.charts = []

    def buy_clothes(self, name, money):
        if self.total_money >= money :
            self.charts.append(name)
            self.total_money = self.total_money - money ;
            print('buy {} success!'.format(name))
        else :
            print('buy {} failed!'.format(name))

    def rechargeMoney(self, money):
        self.total_money += money ;