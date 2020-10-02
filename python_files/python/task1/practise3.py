#5 задача банковский вклад Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).

summ = float(input('Введите сумму : '))
year = int(input('Введите срок : '))

def bank(a, years):
    newsum = a
    for i in range(years):
        newsum = newsum + newsum*0.1
    return newsum

test = bank(summ, year)

print(test)
