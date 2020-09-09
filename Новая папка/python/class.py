# работа с классами 

class Name:

    def __init__ (self, name, age, gender, position):
        self.name = name
        self.age = age
        if gender[0].lower() == 'м':
            self.gender = 'мужской'
        elif gender[0].lower() == 'ж':
            self.gender = 'женский'
        else:
            self.gender = 'не опрделенный'
        self.position = position

        print(f'Зарегестирован новый сотрудник компании XXX - {self.name}, возрастом {str(self.age)}, {self.gender} пол, с должностью - {self.position}')

    def submit_work(self, work):
        self.work = work
        print(f'Работа "{self.work}", сотрудника {self.name}, должностью {self.position} успешно отправлена на проверку')

    def verification_work(self):
        print(f'Вам прислали работу "{self.work}", сотрудника {self.name}, должностью {self.position}')
        number = int(input('Поставьте оценку (от 0 до 10) : '))
        while (number > 10 ) or (number < 0):
            print('Введите оценку от 0 до 10')
            number = int(input('Поставьте оценку : '))
        edit = input('Введите недочеты работа, если они есть : ')
        self.rate = f'Ваша оценка {number} \nВаши недочеты {edit}'
    
    def your_rate(self):
        print(self.rate)

employee = Name('Ivan', 22, 'sdf', 'сотрудник')

employee.submit_work('Докладная')

employee.verification_work()

employee.your_rate()