'''На этот раз мы хотим написать вычисления с использованием функций и получить результаты. 
Давайте посмотрим на несколько примеров.:'''
def zero(p = None): return 0 if p is None else int(p(0))
def one(p = None): return 1 if p is None else int(p(1))
def two(p = None): return 2 if p is None else int(p(2))
def three(p = None): return 3 if p is None else int(p(3))
def four(p = None): return 4 if p is None else int(p(4))
def five(p = None): return 5 if p is None else int(p(5))
def six(p = None): return 6 if p is None else int(p(6))
def seven(p = None): return 7 if p is None else int(p(7))
def eight(p = None): return 8 if p is None else int(p(8))
def nine(p = None): return 9 if p is None else int(p(9))

def plus(v): return lambda x: x + v
def minus(v): return lambda x: x - v
def times(v): return lambda x: x * v
def divided_by(v): return lambda x: x // v
