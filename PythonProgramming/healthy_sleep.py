# Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки,
# но пересыпать тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов
# в сутки. Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите
# “Это нормально”. Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.
# Получаемое число A всегда меньше либо равно B.
# На вход программе в три строки подаются переменные в следующем порядке: A, B, H.
# Обратите внимание на регистр символов: вывод должен в точности соответствовать описанному
# в задании, т. е. если программа должна вывести "Пересып", выводы программы
# "пересып", "ПЕРЕСЫП", "ПеРеСыП" и другие не будут считаться верными.
# Это первое не самое тривиальное задание на условное выражение. В случаях, когда разбить исполнение
# программы на несколько направлений, стоит внимательно обдумать все условия, которые нужно использовать.
# Особое внимание стоит уделить строгости используемых условных операторов:
# различайте \lt< и \le≤; \gt> и \ge≥. Для того, чтобы понимать,
# какой из них стоит использовать, внимательно прочитайте условие задания.


def healthy_sleep():
    a, b, h = (int(input()) for i in range(3))
    if h < a:
        print('Недосып')
    elif h > b:
        print('Пересып')
    else:
        print('Это нормально')


if __name__ == '__main__':
    healthy_sleep()