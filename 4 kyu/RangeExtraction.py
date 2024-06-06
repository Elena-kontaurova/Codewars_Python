'''Формат для выражения упорядоченного списка целых чисел заключается в использовании списка, разделенного запятыми, либо
индивидуальные целые числаили диапазон целых чисел, обозначаемый начальным целым числом, отделенным от конечного 
целого числа в диапазоне чертой, '-'. 
Диапазон включает все целые числа в интервале, включая обе конечные точки. Диапазон не считается диапазоном, 
если он не охватывает как минимум 3 числа. Например, "12,13,15-17"
Завершите решение так, чтобы оно принимало список целых чисел в порядке возрастания и возвращало правильно отформатированную 
строку в формате диапазона.'''
def solution(args):
    result = []
    prev = args[0] - 1
    start = args[0]
    
    for num in args:
        if num == prev + 1:
            prev = num
        else:
            if prev == start:
                result.append(str(start))
            elif prev == start + 1:
                result.append(str(start) + "," + str(prev))
            else:
                result.append(str(start) + "-" + str(prev))
            start = num
            prev = num
    
    if prev == start:
        result.append(str(start))
    elif prev == start + 1:
        result.append(str(start) + "," + str(prev))
    else:
        result.append(str(start) + "-" + str(prev))
    
    return ",".join(result)
