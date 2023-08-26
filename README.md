# principles_of_Software



## Conversion system
```python
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

```

This class represents a Shekel currency object. It has two attributes: `value`, which stores the value of the currency, and `__str__`, which returns a string representation of the currency. The `__add__` and `__sub__` methods implement the addition and subtraction operators for Shekel objects.

```python
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

```

This class represents a Dollar currency object. It has two attributes: `value`, which stores the value of the currency, and `__str__`, which returns a string representation of the currency. The `__add__` and `__sub__` methods implement the addition and subtraction operators for Dollar objects.

```python
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

```

This class represents a Euro currency object. It has two attributes: `value`, which stores the value of the currency, and `__str__`, which returns a string representation of the currency. The `__add__` and `__sub__` methods implement the addition and subtraction operators for Euro objects.

```python
Shekel(100)
Dollar(50)
Euro(80)
print(Shekel(100),Dollar(50),Euro(80))

rates ={('dollar', 'nis'): 3.45,('euro','nis'): 3.67}

rates[('euro','dollar')]=rates[('euro','nis')]/rates[('dollar', 'nis')]

def type_tag(x):
 return type_tag.tags[type(x)]

type_tag.tags = {Shekel: 'nis',Dollar: 'dollar', Euro: 'euro'}

```

This code defines a dictionary `rates` that maps currency pairs to exchange rates. It also defines a function `type_tag` that returns the currency tag for a given object. Finally, it sets the `tags` attribute of the `type_tag` class to a dictionary that maps currency classes to their corresponding tags.

```python
def apply(operation, obj1,obj2):
    """
    :param operation:The calculation operator we will use
    :param obj1: The object of the coin
    :param obj2: The object of the coin
    :return: the final calculation of the two types of coins (according to the operator)
    """
    if operation != 'add':
        raise ValueError("Invalid operation")
    if type_tag(obj1) == 'nis' or type_tag

##calculator

* It can evaluate expressions that contain the following operators: `+`, `-`, `*`, `/`, `ror`
* It can evaluate expressions that contain parentheses
* It can handle numbers, variables, and nested expressions

The code is well-formatted and easy to read. It uses functions to organize the code and make it easier to maintain. The functions are well-named and easy to understand.

The code could be improved in a few ways:

* It could be more user-friendly by providing better error messages.
* It could be more efficient by using data structures to store the expression tree.
* It could be extended to support more features, such as variables and functions.

Overall, the code is well-written and easy to understand. It is a good example of how to implement a simple calculator in Python.

Here are some additional explanations about the code:

* The `calc_eval` function evaluates an expression tree by recursively calling itself on the operands of the expression.
* The `calc_apply` function applies an operator to a list of operands.
* The `read_eval_print_loop` function repeatedly prompts the user for an expression and then prints the result of evaluating the expression.
* The `calc_parse` function converts a string expression into an expression tree.
* The `tokenize` function tokenizes a string expression.
* The `analyze` function analyzes a tokenized expression and returns an expression tree.
* The `assert_non_empty` function raises an error if the given list is empty.
* The `analyze_token` function analyzes a token and returns its type and value.
* The `analyze_operands` function analyzes a list of tokens and returns a list of operands.
