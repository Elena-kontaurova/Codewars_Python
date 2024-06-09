'''Учитывая n x n массив, верните элементы массива, расположенные 
от крайних элементов к среднему элементу, перемещаясь по часовой стрелке.
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
Для лучшего понимания, пожалуйста, последовательно следуйте номерам следующего массива:
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]'''
def snail(snail_map):
    result = []
    while snail_map:
        result += snail_map.pop(0)
        for row in snail_map:
            if row:
                result.append(row.pop())
        if not snail_map:
            break
        result += snail_map.pop()[::-1]
        for row in snail_map[::-1]:
            if row:
                result.append(row.pop(0))
    return result
