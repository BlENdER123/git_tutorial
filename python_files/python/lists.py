contacts = {
    'Anton' : '+79787987987',
    'Ivan' : '+9-0080800990',
    'Dima' : '+234234234234'
}

name = input('Введите имя сотрудника : ')

if name in contacts: 
    print('Контактс найден \n' + name + ' : ' + contacts[name])
else:
    print('Контакт не найден!')