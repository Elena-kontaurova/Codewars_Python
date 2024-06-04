'''Ваша функция productFib принимает целое число (prod) и возвращает массив:
[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
в зависимости от языка, если F(n) * F(n+1) = результат.
Если вы не найдете двух последовательных подтверждающих F (n), F(n) * F(n+1) = prodвы вернетесь
[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) - наименьшее значение, такое как F(n) * F(n+1) > prod.'''
def product_fib(_prod):
    a, b = 0, 1
    while a* b < _prod:
        a,b = b, a + b
    return [a,b, a*b == _prod]
