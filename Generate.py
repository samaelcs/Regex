from pythonds.basic.stack import Stack
import random
import string

exp = '( ( ( a + null ) | ( b * null ) ) . c )'

Parent = Stack()
Ch = Stack()
Operator = Stack()


def Convert(exp):
    ListExp = exp.split()
    Production = {}
    NonTerminals = list(string.ascii_uppercase)
    start = True

    for i in ListExp:

        if i == '(':
            Parent.push('(')

        elif i == ')':
            Parent.pop()
            op = Operator.pop()
            right = Ch.pop()
            left = Ch.pop()

            if start == True:
                NT = 'S'
                del NonTerminals[NonTerminals.index('S')]
                start = False
            else:
                NT = random.choice(NonTerminals)
                del NonTerminals[NonTerminals.index(NT)]

            if op == '|':
                Production[NT] = [left, right]
            elif op == '.':
                Production[NT] = [left+right]
            elif op == '*':
                Production[NT] = [NT+left, 'EPSILON']
            elif op == '+':
                Production[NT] = [left+NT, left]
            Ch.push(NT)
        elif i in ['*', '+', '|', '.']:
            Operator.push(i)
        else:
            Ch.push(i)

    for key in Production.keys():
        print(key, ' --> ', end = '')
        for i in range(len(Production[key])):
            if not (i == len(Production[key]) - 1):
                print(Production[key][i], ' | ', end = '')
            else:
                print(Production[key][i], end = '')
        print()

Convert(exp)