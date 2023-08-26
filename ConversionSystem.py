class Shekel:
    """
    A currency object
    """
    def __init__(self, value):
        """
        :param value: the value of the currency
        """
        self.value = value

    def __str__(self):
        return "{:0.1f}₪".format(self.value)

    def __repr__(self):
        return f"Shekel({self.value})"

    def __add__(self, other):
        return coerce_apply('add', self, other)

    def __sub__(self, other):
        return coerce_apply('sub', self, other)

class Dollar:
    """
    A currency object
    """
    def __init__(self, value):
        """
        :param value: the value of the currency
        """
        self.value = value

    def __str__(self):
        return "{:0.1f}$".format(self.value)

    def __repr__(self):
        return f"Dollar({self.value})"

    def __add__(self, other):
        return coerce_apply('add', self, other)

    def __sub__(self, other):
        return coerce_apply('sub', self, other)

class Euro:
    """
    A currency object
    """
    def __init__(self, value):
        """
        :param value:the value of the currency
        """
        self.value = value

    def __str__(self):
        return "{:0.1f}€".format(self.value)

    def __repr__(self):
        return f"Euro({self.value})"

    def __add__(self, other):
        return coerce_apply('add', self, other)

    def __sub__(self, other):
        return coerce_apply('sub', self, other)

Shekel(100)
Dollar(50)
Euro(80)
print(Shekel(100),Dollar(50),Euro(80))


rates ={('dollar', 'nis'): 3.45,('euro','nis'): 3.67}

rates[('euro','dollar')]=rates[('euro','nis')]/rates[('dollar', 'nis')]

def type_tag(x):
 return type_tag.tags[type(x)]

type_tag.tags = {Shekel: 'nis',Dollar: 'dollar', Euro: 'euro'}

def apply(operation, obj1,obj2):
    """
    :param operation:The calculation operator we will use
    :param obj1: The object of the coin
    :param obj2: The object of the coin
    :return: the final calculation of the two types of coins (according to the operator)
    """
    if operation != 'add':
        raise ValueError("Invalid operation")
    if type_tag(obj1) == 'nis' or type_tag(obj2) == 'nis':

        if type_tag(obj1) != 'nis':obj1.value=obj1.value*rates[(type_tag(obj1), 'nis')]
        if type_tag(obj2) != 'nis': obj2.value = obj2.value * rates[(type_tag(obj2), 'nis')]
        return Shekel(obj1.value+obj2.value)

    elif type_tag(obj1) == 'dollar' or type_tag(obj2) == 'dollar':

        if type_tag(obj1) != 'dollar': obj1.value = obj1.value * rates[(type_tag(obj1), 'dollar')]

        if type_tag(obj2) != 'dollar': obj2.value = obj2.value * rates[(type_tag(obj2), 'dollar')]
        return Dollar(obj1.value + obj2.value)
    else:
        return  Euro(obj1.value + obj2.value)

apply('add', Euro(100), Shekel(200)) # Shekel(567.0)
apply('add', Dollar(30), Shekel(50))  # Shekel(153.5)
print(apply('add',Euro(30),Dollar(50)))


def coerce_apply(operation, obj1,obj2):
    """
    :param operation:Type of operator to be received
    :param obj1: The object of the coin
    :param obj2: The object of the coin
    :return:
    """
    total_val=0
    result_currency = 'dollar'
    if operation not in ('add', 'sub'):
        raise ValueError("Invalid operation")
    if operation == 'add':
         return apply('add',obj1,obj2)
    else:
        obj2.value*=-1
        return apply('add', obj1, obj2)

coerce_apply('add',Euro(100), Euro (200))
coerce_apply('add',Dollar(30),Shekel(50))
print(coerce_apply('add',Euro(30),Dollar(50)))
coerce_apply('sub',Euro(100),Shekel(200))
print(coerce_apply('sub',Shekel(200),Dollar(100)))
print(coerce_apply('add',Euro(50),Dollar(30)))


Euro(100) + Euro (200)
Dollar(30) + Shekel(50)
print(Shekel(200) + Euro(100))
print(Euro(30) + Dollar(50))
Euro(100) - Shekel(200)
print(Shekel(200) - Dollar(100))
