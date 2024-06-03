'''Реализуйте функцию unique_in_order, которая принимает в качестве аргумента последовательность 
и возвращает список элементов без каких-либо элементов с одинаковым значением рядом друг с другом и 
сохраняет исходный порядок элементов.'''
def unique_in_order(sequence):
    s = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i -1]:
            s.append(sequence[i])
    return s
