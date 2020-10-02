#Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
sec = 100001

def secfunc(sec):
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    while sec > 60:
        sec -= 60
        minutes += 1
        while minutes > 60:
            minutes -= 60
            hours += 1
            while hours > 24:
                hours -= 24
                days += 1
    
    return sec,minutes,hours,days

test = secfunc(sec)

print(f'{str(test[3])}:{str(test[2])}:{str(test[1])}:{str(test[0])}')
