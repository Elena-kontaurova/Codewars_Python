'''Напишите функцию, dirReduc которая примет массив строк и вернет массив строк с удаленными ненужными указаниями
(W<->E или S<->N рядом).
Версия для Haskell содержит список указаний с data Direction = North | East | West | South.
Версия Clojure возвращает nil, когда путь сводится к нулю.
Версия Rust занимает часть enum Direction {North, East, West, South}.'''
def dir_reduc(arr):
    d = {'NORTH':'SOUTH', 'SOUTH':'NORTH', 'EAST':'WEST', 'WEST':'EAST'}
    for i in range(len(arr)-1):
        if d[arr[i]] == arr[i+1]:
            del arr[i:i+2]
            return dir_reduc(arr)
    return arr
