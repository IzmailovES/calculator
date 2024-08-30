#!/usr/bin/env python3

from string import digits,ascii_letters



class ExprItem:
    def __init__(self, s):
        self.strlen = len(s)

    def __repr__(self):
        return str(type(self)) + ': ' + str(self.value)

class Number(ExprItem):
    def __init__(self, s):
        super().__init__(s)
        self.value = float(s)

class Operator(ExprItem):
    operator_priority = {'(' : 0, # чтобы не было ошибок пи парсинге
                             '+' : 1,
                             #'-' : 1, заменен та унарный минус
                             '*' : 2,
                             '/' : 2,
                             '^' : 3,
                             '-' : 4,
                            'sin' : 5,
                            'cos' : 6,
                            'tan' : 6,
                            'log' : 6,
                            'sqrt' : 6,
                            'exp' : 6
                         }
    def __init__(self,s):
        super().__init__(s)
        self.value = s
        self.priority = Operator.operator_priority[self.value]

class Bracket(ExprItem):
    def __init__(self, s):
        super().__init__(s)
        self.value = s


class Variable(ExprItem):
    known_vars = dict()
    def __init__(self, s):
        super().__init__(s)
        self.value = s

    @classmethod
    def update(cls, var_name, var_val):
        cls.known_vars[var_name] = var_val


def parse_item(s):
    p = 0
    while s[p] in digits + '.':
        p += 1
    if p > 0:
        return Number(s[:p])

    if s[p] in '()':
        return Bracket(s[p])

    for op in Operator.operator_priority:
        if s.startswith(op):
            return Operator(op)

    while s[p] in ascii_letters:
        p += 1
    return Variable(s[:p])


s = '(1+1)*x+sin(123)'
p = 0
ret = list()
while p < len(s):
    item = parse_item(s[p:])
    ret.append(item)
    p += item.strlen

print(ret)






