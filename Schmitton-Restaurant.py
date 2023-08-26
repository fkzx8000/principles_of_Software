def make_instance(cls):

    attrs = {}
    def set(name, val):

        attrs[name] = val
    def get(name):

        if name in attrs:
            return attrs[name]
        else:
            val = cls['get'](name)
            return bind_method(val, instance)
    instance = {'get': get, 'set': set}
    return instance

def bind_method(val, instance):

    if callable(val):
        def method(*args):

            return val(instance, *args)
        return method
    return val

def make_class(attrs, base=None):

    def set(name, val):

        attrs[name] = val
    def get(name):

        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    def new(*args):

        return init_instance(cls, *args)
    cls = {'set': set, 'get': get, 'new': new}
    return cls

def init_instance(cls, *args):

    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance

def make_item_class():

    def init(self, name, price, calories):

        self['set']('name', name)
        self['set']('price', price)
        self['set']('calories', calories)

    def __str__(self):
        """
        :param self:This is the instance of the Item class.
        :return:string
        """
        return "({}:{}$:{}cal)".format(self['get']('name'), self['get']('price'), self['get']( 'calories'))

    return make_class({'__init__': init, '__str__': __str__})

def make_order_class():

    def init(self, name,menu=None, order_list=None):

        self['set']('name', name)
        self['set']('menu', menu)
        if order_list == None and menu:
            self['set']('order_list', menu)
        if menu != None and order_list:
            items = []
            for i in order_list:
                items.append(menu[i - 1])
                self['set']('order_list' , items)

    def add_items(self, menu1=None, selected_products=None):

        items = []
        if menu1:
            self['set']('menu',menu1)
        if type(selected_products) == type(tuple()):
            for i in selected_products:
                items.append(menu1[i - 1])
        self['set']('order_list',list(items))

    def remove_item(self, index):

        print("Remove Item from order: {}".format(self['get']('order_list')[index-1]['get']('__str__')()))
        self['get']('order_list').pop(index-1)

    def __str__(self):
    
        temp_str=""
        for size in range(len(self['get']('order_list'))):
            temp_str += self['get']('order_list')[size]['get']('__str__')()
        return "({}, ({}), total:{}$, calories:{}cal)".format(self['get']('name'), temp_str,self['get']('total')(),self['get']('calories')())

    def total(self):

        sum_total=0
        for size in range(len(self['get']('order_list'))):
            sum_total += self['get']('order_list')[size]['get']('price')
        return sum_total

    def calories(self):

        sum_total=0
        for size in range(len(self['get']('order_list'))):
            sum_total += self['get']('order_list')[size]['get']('calories')
        return sum_total

    return make_class({'__init__': init, '__str__': __str__, 'add_items': add_items, 'remove_item': remove_item,'total':total,'calories':calories})

def make_restaurant_class():

    def init(self, name, menu,orders=None):

        self['set']('Restaurant_name', name)
        self['set']('menu', menu)
        self['set']('orders', orders)

    def add_menu(self, add_item):

        self['get']('menu').append(add_item)

    def remove_menu(self, index):

        item = self['get']('menu')[index-1]
        self['get']('menu').pop(index-1)
        print("Remove Item from menu:", item['get']('__str__')())

    def print_menu(self):

        print("Menu:")
        menu = self['get']('menu')
        for i in range(len(menu)):
            item = menu[i]
            tempstr = "{0}) {1:<15s} {2:>5d}$ {3:>6d}cal".format(i + 1, item['get']('name'), item['get']('price'),item['get']('calories'))
            print(tempstr)

    def add_orders(self, orders_obj):

        if type(orders_obj) == type(tuple()):
            for i in range(len(orders_obj)):
                self['get']('orders').append(orders_obj[i])
        else:
            self['set']('orders', [])
            self['get']('orders').append(orders_obj)

    def print_orders(self):
        """
        The method print orders
        :param self: This is the instance of the Restaurant class.
        """
        for order in self['get']('orders'):
            print(order['get']('__str__')())

    def __str__(self):
        """
        :param self: This is the instance of the Restaurant class.
        :return: string representation of the Restaurant instance.
        """
        temp_str=""
        for size in range(len(self['get']('menu'))):
            temp_str += self['get']('menu')[size]['get']('__str__')()
        return "({},({})())".format(self['get']('Restaurant_name'),temp_str)

    return make_class({'__init__': init, '__str__': __str__, 'add_menu': add_menu, 'remove_menu': remove_menu, 'print_menu': print_menu, 'add_orders': add_orders, 'print_orders': print_orders})

def min_calories1(rest):

    index = rest['get']('orders')[0]
    if rest['get']('orders'):
        for i in range(1, len(rest['get']('orders'))):
            if rest['get']('orders')[i]['get']('calories')() < index['get']('calories')():
                index = rest['get']('orders')[i]
        print(index['get']('__str__')())
        return index
    else:
        return "There are no reservations"

ItemClass = make_item_class()
OrderClass = make_order_class()
RestaurantClass = make_restaurant_class()

item1=ItemClass['new']('Big Mac',10,550)
item1['get']('price')
print(item1['get']('__str__')())
menu1=[ItemClass['new']('McDouble',10,400),ItemClass['new']('Big_Mac',12,550),ItemClass['new']('McChicken',10,400),ItemClass['new']('Fries',5,320),ItemClass['new']('Cappuccino',3,160), ItemClass['new']('Coca-Cola',5,210)]
order1=OrderClass['new']('David')
order1['get']('add_items')(menu1,(1,3,5))
print(order1['get']('__str__')())
order1['get']('remove_item')(1)
print(order1['get']('__str__')())
order2=OrderClass['new']('Tali',menu1,(2,4,5,6))
print(order2['get']('__str__')())

rest1=RestaurantClass['new']('BurgerPoint',menu1)
print(rest1['get']('__str__')())
rest1['get']('add_menu')(ItemClass['new']('Green_Salad',12,434))
rest1['get']('remove_menu')(1)
rest1['get']('print_menu')()
rest1['get']('add_orders')(OrderClass['new']('David',rest1['get']('menu'),(2,4,5,6)))
rest1['get']('add_orders')((OrderClass['new']('Tali',rest1['get']('menu'),(1,3,5)),OrderClass['new']('Jim',rest1['get']('menu'),(1,2,3,5))))
rest1['get']('print_orders')()

min_calories1(rest1)['get']('__str__')()


