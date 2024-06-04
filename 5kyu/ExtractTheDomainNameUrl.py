'''Напишите функцию, которая при задании URL в виде строки
анализирует только имя домена и возвращает его в виде строки.'''
def domain_name(url):
    url = url.replace('http://', '').replace('www.', '').replace('https://', '')
    return url.split('.')[0]
