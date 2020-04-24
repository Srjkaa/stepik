# Паша очень любит кататься на общественном транспорте, а получая билет,
# сразу проверяет, счастливый ли ему попался. Билет считается счастливым,
# если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать
# программу, которая проверит равенство сумм и выведет "Счастливый",
# если суммы совпадают, и "Обычный", если суммы различны.
# На вход программе подаётся строка из шести цифр.
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

def is_lucky(num):
    firstPart = num // 100000 + num % 100000 // 10000 + num % 10000 // 1000
    secondPart = num % 1000 // 100 + num % 100 // 10 + num % 10
    print('Счастливый' if firstPart == secondPart else 'Обычный')


if __name__ == '__main__':
    is_lucky(int(input()))