#!/usr/bin/env python3

from string import digits



class ExprItem:
    def __init__(self, s):
        self.strlen = len(s)

    def __repr__(self):
        return ' ' + str(self.value) + ' '

class Number(ExprItem):
    def __init__(self, s):
        super().__init__(s)
        self.value = float(s)

class Operator(ExprItem):
    operator_priority = dict('(' : 0, # чтобы не было ошибок пи парсинге
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
                            )
    def __init__(self):
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

    



