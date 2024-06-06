'''Ваша задача для выполнения этого ката - написать функцию, которая форматирует длительность, 
заданную в виде количества секунд, удобным для человека способом.
Функция должна принимать неотрицательное целое число. Если оно равно нулю, она просто возвращает значение "now". 
В противном случае продолжительность выражается в виде комбинации years, days, hours minutes и seconds..'''
def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    years = seconds // (365 * 24 * 60 * 60)
    days = (seconds % (365 * 24 * 60 * 60)) // (24 * 60 * 60)
    hours = (seconds % (24 * 60 * 60)) // (60 * 60)
    minutes = (seconds % (60 * 60)) // 60
    seconds = seconds % 60
    
    time_units = [('year', years), ('day', days), ('hour', hours), ('minute', minutes), ('second', seconds)]
    time_format = [f"{value} {unit}" if value == 1 else f"{value} {unit}s" for unit, value in time_units if value > 0]
    
    return ', '.join(time_format[:-1]) + ' and ' + time_format[-1] if len(time_format) > 1 else time_format[0]
