
```markdown
# Code Comparison

This file compares two versions of a Python code: the normal version and the Schmitton version.

## Normal Version

The normal version of the code uses traditional Python syntax. It defines three classes: `Item`, `Order`, and `Restaurant`.

The `Item` class represents an item on a menu. It has three attributes: `name`, `price`, and `calories`.

The `Order` class represents an order. It has three attributes: `name`, `menu`, and `order_list`. The `menu` attribute is a list of `Item` objects. The `order_list` attribute is a list of the items that have been ordered.

The `Restaurant` class represents a restaurant. It has three attributes: `name`, `menu`, and `orders`. The `menu` attribute is a list of `Item` objects. The `orders` attribute is a list of `Order` objects.

## Schmitton Version

The Schmitton version of the code uses a different syntax called Schmitton. Schmitton is a functional programming language that is based on Python.

The Schmitton version of the code defines the same three classes as the normal version. However, the syntax is different.

For example, the `Item` class is defined as follows in Schmitton:

```
def make_item_class():

     attrs = {}
     def set(name, val): attrs[name] = val
     def get(name):
         if name in attrs:
             return attrs[name]
         otherwise:
             val = cls'get': name
             return bind_method(val, instance)
     instance = {'get': get, 'set': set}
     return instance


The `set` and `get` functions are used to set and get the attributes of an object. The `bind_method` function is used to bind a method to an object.

## Differences

The main difference between the normal version and the Schmitton version of the code is the syntax. The Schmitton version uses a functional programming style, while the normal version uses a traditional Python style.

Another difference is that the Schmitton version uses a custom `make_class` function to create classes. This function makes it easier to create classes in Schmitton.

Finally, the Schmitton version uses a custom `make_instance` function to create instances of classes. This function makes it easier to create instances of classes in Schmitton.

## Conclusion

The two versions of the code are functionally equivalent. However, the Schmitton version is more concise and easier to read.

# principles_of_Software

This repository contains two Python programs:

* `conversion_system.py` implements a conversion system for three currencies: Shekels, Dollars, and Euros.
* `calculator.py` implements a simple calculator that can evaluate expressions that contain the following operators: `+`, `-`, `*`, `/`, `ror`.

## Conversion system

The `conversion_system.py` program defines three classes: `Shekel`, `Dollar`, and `Euro`. Each class represents a currency and has two attributes: `value`, which stores the value of the currency, and `__str__`, which returns a string representation of the currency. The `__add__` and `__sub__` methods implement the addition and subtraction operators for each currency.

The program also defines a dictionary `rates` that maps currency pairs to exchange rates. For example, the entry `('dollar', 'nis')` maps the pair `dollar` and `nis` to the exchange rate of 3.45.

The program can be used to convert between currencies. For example, the following code converts 100 Shekels to Dollars:

python
shekel = Shekel(100)
dollar = shekel.to_dollars()
print(dollar)
```

The output of the code is:

```
345.0


## Calculator

The `calculator.py` program defines several functions for evaluating expressions:

* `calc_eval` evaluates an expression tree.
* `calc_apply` applies an operator to a list of operands.
* `read_eval_print_loop` repeatedly prompts the user for an expression and then prints the result of evaluating the expression.
* `calc_parse` converts a string expression into an expression tree.
* `tokenize` tokenizes a string expression.
* `analyze` analyzes a tokenized expression and returns an expression tree.
* `assert_non_empty` raises an error if the given list is empty.
* `analyze_token` analyzes a token and returns its type and value.
* `analyze_operands` analyzes a list of tokens and returns a list of operands.

The program can be used to evaluate expressions. For example, the following code evaluates the expression `1 + 2 * 3`:

python
expression = "1 + 2 * 3"
tree = calc_parse(expression)
result = calc_eval(tree)
print(result)
```

The output of the code is:

```
7


## Principles of software engineering

The two programs in this repository demonstrate the following principles of software engineering:

* **Modularity:** The programs are divided into modules that each perform a specific task. This makes the programs easier to understand, maintain, and extend.
* **Abstraction:** The programs use abstractions to hide the details of how things work. This makes the programs easier to use and understand.
* **Encapsulation:** The programs encapsulate data and functionality into objects. This makes the programs easier to maintain and extend.
* **Testability:** The programs are written in a way that makes them easy to test. This helps to ensure that the programs work correctly.
* **Reusability:** The programs are written in a way that makes them easy to reuse. This helps to reduce the amount of code that needs to be written.

