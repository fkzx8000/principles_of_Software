
class Item:
    """
    The Item class is a simple class that represents an item on a menu.
     It has three data attributes: name, price, and calories.
      It also has several methods for accessing and manipulating these attributes,
        such as a constructor, a string representation method, and methods for getting the price and calories of the item.
        It is intended to be used as a base class for other classes that need to represent items on a menu.
    """

    def __init__(self, name, price, calories):
        """
        :param name: This is the name of the item.
        :param price: This is the price of the item.
        :param calories: This is the calorie count of the item.
        """
        self.name = name
        self.price = price
        self.calories = calories

    def __str__(self):
        """
        :return:string representation of the instance.
        Generic function that shows the values of the product
        """
        return f"({self.name}:{self.price}$:{self.calories}cal)"

    def __repr__(self):
        """Generic function that shows the values of the product"""
        return "Item('{0}',{1},{2})".format(self.name,self.price,self.calories)

    def getPrice(self):
        """
        :return: the price of the product
        """
        return self.price

    def getcalories(self):
        """Returns the calories to the product"""
        return self.calories

class Order(Item):

    def __init__(self,name,menu=None,order_list=None):
        """
        :param self: This is the instance of the Order class being initialized
        :param name: This is the name of the person placing the order.
        :param menu: This is the menu of items that can be ordered. It is an optional argument and is set to None by default.
        :param order_list: This is the list of items that have been ordered. It is an optional argument and is set to None by default.
        """
        self.name = name
        self.menu = menu
        if order_list == None and menu:
            self.order_list=menu
        if menu != None and order_list:
            items = []
            for i in order_list:
                items.append(menu[i - 1])
                self.order_list = items

    def __str__(self):
        """Generic function to return string values of the object"""
        if self.order_list:
            temp=tuple(self.order_list)
            strr="({}, (".format(self.name)
            for i in range(len(self.order_list)):
                strr += str(self.order_list[i])
                if i < len(self.order_list)-1:
                    strr+=","
            strr+="), total:{}$, calories:{}cal)".format(self.total(),self.calories())
        return strr

    def __repr__(self):
        """
        A generic function for printing the values of the object, it uses a loop to represent the content exactly in the EVAL shell
        :return: Order('name',[Item('name of item',10,400), Item('name of item',3,160)])
        """
        if self.order_list:
            Temp_str="Order('{}',[".format(self.name)
            for i in range(len(self.order_list)):
                 Temp_str += "{}".format(repr(self.order_list[i]))
                 if i < len(self.order_list) - 1:
                    Temp_str += ", "
            Temp_str += "])"
            return Temp_str

    def add_items(self, menu, tup=None):
        """
        :param self: This is the instance of the Order class.
        :param menu: This is a new menu of items that can be ordered. It is an optional argument and is set to None by default.
        :param tup: This is a tuple of indices of items in menu1 that are to be added to the order_list attribute.
                It is an optional argument and is set to None by default.
     """
        items = []
        self.menu=menu
        if type(tup) == type(tuple()):
            for i in tup:
                items.append(menu[i-1])
            self.order_list=list(items)
        elif type(tup) == type(Item):
            print("item")

        return self.order_list

    def remove_item(self, index):
        """
        :param self: This is the instance of the Order class.
        :param index: This is the index of the item in order_list that is to be removed.
        """
        print("Remove Item: {}".format(self.order_list[index-1]))
        self.order_list.pop(index-1)

    def total(self):
        """
        :param self:This is the instance of the Order class.
        :return:total price of the items in the order_list attribute.
        """
        sum=0
        Mylist=list(self.order_list)
        for i in Mylist:
           sum=sum+i.getPrice()
        return sum

    def calories(self):
        """
        :param self:This is the instance of the Order class.
        :return:total number of calories of the items in the order_list attribute.
        """
        sum=0
        Mylist=list(self.order_list)
        for i in Mylist:
           sum=sum+i.getcalories()
        return sum

class Restaurant(Order,Item):

    def __init__(self, name, menu, orders=None):
        """A constructor that accepts product values and puts them into an object"""
        self.Restaurant_name = name
        self.menu = menu
        if orders:
            self.Rest_orders = orders
        else:
            self.Rest_orders = None

    def __repr__(self):
        """A constructor that accepts product values and puts them into an object"""
        if self.menu:
            Temp_str = "Restaurant('{}',{},[])".format(self.Restaurant_name, self.menu)
            return Temp_str

    def add_menu(self,add_item):
        """The function receives an argument in this case "Add Item" and adds it to the menu"""
        self.menu.append(add_item)
        return self.menu

    def remove_menu(self,index):
        """The function gets an index in this case and deletes it from the menu"""
        print("Remove Item from menu:", self.menu[index-1])
        self.menu.pop(index-1)
        return self.menu

    def print_menu(self):
        print("Menu:")
        """This function prints all the details in the menu, numbers them and records their price and the amount of calories"""
        for i in range(len(self.menu)):
            tempstr = "{0}) {1:<15s} {2:>5d}$ {3:>6d}cal".format(i + 1, self.menu[i].name, self.menu[i].price, self.menu[i].calories)
            print(tempstr)

    def add_orders(self,order_obj):
        """This function receives orders,
         if it received a quantity of "Tuple" orders,
         it breaks it down into single objects and adds to the list,
         if it received a single tuple,
        it simply adds it"""
        if self.Rest_orders and type(order_obj) == type(tuple()):
            for i in range(len(order_obj)):
                self.Rest_orders.append(order_obj[i])
        else:
            self.Rest_orders = []
            self.Rest_orders.append(order_obj)
        return self.Rest_orders

    def print_orders(self): [print(f'{x}') for x in self.Rest_orders];"""This function knows how to print all existing orders in the restaurant, including the price for each order and the amount of calories"""

def min_calories(rest): return min(rest.Rest_orders, key=lambda x: x.calories()) if rest.Rest_orders else 'There are no reservations';"""This function accepts a restaurant as a parameter and returns an order with a minimum amount of calories or a message
There are no reservations"""

item1=Item('Big Mac',10,550)
item1.price
#10
item1
#Item('Big Mac',10,550)
print(item1)
#(Big Mac:10$:550cal)
item2=eval(repr(item1))
item2
#Item('Big Mac',10,550)
menu=[Item('McDouble',10,400),Item('Big_Mac',12,550),Item('McChicken',10,400),Item('Fries',5,320),Item('Cappuccino',3,160),Item('Coca-Cola',5,210)]
order1=Order('David')
order1.add_items(menu,(1,3,5))
order1
#Order('David',[Item('McDouble',10,400), Item('McChicken',10,400), Item('Cappuccino',3,160)])
print(order1)
#(David, ((McDouble:10$:400cal),(McChicken:10$:400cal),(Cappuccino:3$:160cal)), total:23$, calories:960cal)
order1.remove_item(1)
#Remove Item: (McDouble:10$:400cal)
order2=eval(repr(order1))
order2.name='Tali'
print(order2)
# #(Tali, ((McChicken:10$:400cal),(Cappuccino:3$:160cal)), total:13$, calories:560cal)
order3=Order('Jim', menu, (2,4,5,6))
print(order3)

rest1=Restaurant('BurgerPoint', menu)
rest1

rest1.add_menu(Item('Green_Salad',12,434))
rest1.remove_menu(1)
rest2=eval(repr(rest1))
rest2.name='BurgerSheva'
rest2

rest1.print_menu()

rest1.add_orders(Order('David',rest1.menu,(2,4,5,6)))
rest1.add_orders((Order('Tali',rest1.menu,(1,3,5)),Order('Jim',rest1.menu,(1,2,3,5))))
rest1.print_orders()

print(min_calories(rest1))
