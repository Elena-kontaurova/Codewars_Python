'''Завершите функцию, scramble(str1, str2) которая возвращает, 
true если часть str1 символов может быть переставлена для соответствия str2, в противном случае возвращает false.'''
def scramble(s1, s2):
    for char in set(s2):
        if s1.count(char) < s2.count(char):
            return False
    return True
