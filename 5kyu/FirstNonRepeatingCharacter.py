'''Напишите функцию с именем first_non_repeating_letter†, которая принимает строковый ввод 
и возвращает первый символ, который нигде не повторяется в строке.
Например, если заданы входные данные 'stress', функция должна вернуть 't', 
поскольку буква t встречается в строке только один раз и является первой в строке.
В качестве дополнительной проблемы заглавные и строчные буквы считаются одним и тем же символом, 
но функция должна возвращать правильный регистр для начальной буквы. 
Например, входные данные 'sTreSS' должны возвращать 'T' результат.'''
def first_non_repeating_letter(s):
    ans = [i for i in s if s.lower().count(i.lower()) == 1]
    return ans[0] if ans else ''
