'''В этом ката вам нужно написать простой декодер азбуки Морзе. Хотя азбука Морзе в настоящее время 
в основном вытеснена голосовыми каналами и цифровыми каналами передачи данных, она по-прежнему используется 
в некоторых приложениях по всему миру.
Азбукой Морзе каждый символ кодируется в виде последовательности "точек" и "тире". 
Например, буква A кодируется как ·−, буква Q кодируется как −−·−, а цифра 1 кодируется как ·−−−−. 
Азбука Морзе не зависит от регистра, традиционно используются заглавные буквы. Когда сообщение написано азбукой Морзе, 
для разделения кодов символов используется один пробел, а для разделения слов - 3 пробела. 
Например, сообщение HEY JUDE азбукой Морзе является ···· · −·−−   ·−−− ··− −·· ·.'''
from preloaded import MORSE_CODE

def decode_morse(morse_code):
    return ' '.join(''.join(MORSE_CODE[i] for i in word.split()) for word in morse_code.strip().split('   '))
