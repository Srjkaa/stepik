# Коля каждый день ложится спать ровно в полночь и недавно узнал,
# что оптимальное время для его сна составляет X минут.
# Коля хочет поставить себе будильник так, чтобы он прозвенел ровно
# через X минут после полуночи, однако для этого необходимо указать
# время сигнала в формате часы, минуты. Помогите Коле определить,
# на какое время завести будильник.


def alarm_clock():
    minutes = int(input())
    print(minutes // 60)
    print(minutes % 60)


if __name__ == '__main__':
    alarm_clock()
