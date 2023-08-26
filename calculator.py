lass Tree():
  def __init__(self, value, nodes=None):
      """
        Given an implementation of a class called Tree that represents a general tree. Each node in the tree has an internal value (value) and a list of children (nodes.)
      """
      self.value = value
      self.nodes = nodes

  def __repr__(self):
      return "Tree({})".format(self.value) if not self.nodes else "Tree({}, {})".format(self.value, self.nodes)

def BuildTree(tree):
    """
    :param tree: is represented as a tuple
    :return:Returns a new tree (instance of Tree) so that leaves They have values
    """
    if isinstance(tree, int):
        return Tree(tree)
    value = 0
    nodes = []
    for node in tree:
        t = BuildTree(node)
        value += t.value
        nodes.append(t)
    return Tree(value, nodes)

def MaxValue(tree):
    """
    :param tree: A show of tree
    :return:the largest value that the leaves have
    """
    return tree.value if not tree.nodes else max(MaxValue(node) for node in tree.nodes)

t=BuildTree((((2, 3), (4, (5, 6, (8, 2))))))
t
MaxValue(t)


from functools import reduce

class Exp(object):

    def __init__(self, operator, operands):
        """
        :param operator: The operator in use
        :param operands: The operands in use
        """
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return "Exp({0},{1})".format(repr*(self.operator), repr**(self.operands))

    def __str__(self):
        operand_strs = ','.join(map(str, self.operands))
        return "{0} ({1})".format(self.operator, operand_strs)

def calc_eval(exp):
    """
    :param exp: or a number, or an object of type Exp
    :return: A number after the mathematical calculation
    """
    str_temp = str(exp)
    if type(exp) in (int, float):
        return exp
    elif type(exp) == Exp:
        arguments = map(calc_eval, exp.operands)

        return calc_apply(exp.operator, arguments) if not exp.operator == 'type' else "<class {}>".format(Exp(1,1).__class__.__name__) if any(substring in str_temp for substring in ['add', 'div', 'mul', 'sub', 'ror']) else str(type(list(arguments)[0]))

def calc_apply(operator, args):
    """
    :param operator: The operator in use
    :param args: The operands in use
    :return:  A number after the mathematical calculation
    """
    argss = list(args)
    if operator in ('type'):
        return "<class {}>".format(argss[0] if not '__main__.Exp' else type(1))

    if operator in ('ror'):
        try:

            if len(str(argss[0]))<3:
                raise ValueError(f"The number {number} is not possible for rotate")

            elif '.' in str(argss[0]) and (len(str(argss[0]).split(".")[0]) < 3 or len(str(argss[0]).split(".")[1]) < 3):
                raise ValueError(f"The number {argss[0]} is not possible for rotate")

            if not isinstance(argss[0], (int, float)):
                raise ValueError(f"The number {argss[0]} is not possible to rotate")

            if not isinstance(argss[1], int):
                raise TypeError(f"{argss[1]} is not <class int>")

            if argss[1] < 0:
                raise ValueError(f"{argss[1]} is not a positive number")

            return int((lambda x: x[0][-int(x[1]):]+x[0][:-int(x[1])])(list(map(str,argss)))) if not '.' in str(list(argss)[0]) else             float((lambda Bdot , Fdot , index: Bdot[-index:] + Bdot[:-index] + "." + Fdot[-index:] + Fdot[:-index])(list((lambda x: x.split('.'))(list(map(str, argss))[0]))[0],list((lambda x: x.split('.'))(list(map(str, argss))[0]))[1],list(argss)[1]))

        except Exception as e:
            raise e

    if operator in ('add', '+'):
        return sum(argss)

    if operator in ('sub', '-'):
        if len(argss) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        return -argss[0] if len(argss) == 1 else argss[0] - argss[1]

    if operator in ('mul', '*'):
        return reduce(lambda x,y:x*y, argss, 1)

    if operator in ('div', '/'):
        if len(argss) != 2:
            raise TypeError(operator + 'requires exactly 2 arguments')
        return argss[0] / argss[1]

def read_eval_print_loop():
    """
     If it weren't for the ending
    """
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            result = calc_eval(expression_tree)
            print(result)
        except (SyntaxError, TypeError, ZeroDivisionError, ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            print('Calculation completed')
            return

def calc_parse(line):
    """
    :param line: contains the expression
    :return: the expression tree after testing
    """
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s):' + ' '.join(tokens))
    return expression_tree

def tokenize(line):
    """
    :param line:A mathematical expression in a string
    :return: Expander for testing and dividing
    """
    spaced =line.replace( '(' , ' ( ' ).replace( ')' , ' ) ').replace(',' , ' , ')
    return spaced.split()

Known_operators=['add','sub','mul','div','+','-','*','/','ror','type']

def analyze(tokens):
    """
    :param tokens:A mathematical expression
    :return: the same expression after checks in Exp obj
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in Known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError("expected '(' after " + token)

        return Exp(token, analyze_operands(tokens))

def assert_non_empty(tokens):
    """
    test tokens is not empty
    """
    if len(tokens)==0:
        raise SyntaxError('unexpected end of line')

def analyze_token(token):
    """
    :param token: the token to be analyzed
    :return: a tuple containing the token's type and its value
    """
    if token in Known_operators:
        return token
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            raise SyntaxError("unexpected token: " + token)

def analyze_operands(tokens):
    """
    :param tokens: a list of tokens, representing an arithmetic expression
    :return: a list of numbers, variables or sub-expressions (in the form of nested lists) that represent the operands
    """
    assert_non_empty(tokens)
    operands=[]
    while(tokens[0] != ')' ):
        if operands and tokens.pop(0) !=',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)
    return operands

read_eval_print_loop()


