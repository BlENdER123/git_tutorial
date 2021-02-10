// Задорожний Антон 219/5
#include <iostream>
#include <string>
#include <time.h>
#include <queue>
#include <vector>
using namespace std;

// массив с возможными городами прибытия
string in_cities[] = { "Москва", "Минск","Киев" };

// структура пассажира с фамилией, номер билет, возрастом, и багажом.
struct Passanger {
    string FIO;
    int number;
    int age;
    bool package;
};
// структура билета с номером билет, датой создания билета, городом прибытия, городом отбытия, регистрацией, посадкой и фио.
struct Ticket {
    int number;
    time_t unix_date;
    string out;
    int in;
    bool reg;
    bool checkup;
    string FIO;
};
// простая функция добавления нового пассажира
Passanger AddPassanger(string FIO_in, int age_in, bool package_in = false)
{
    // создаем новый экземпляр пассажира и записываем все переданные данные
    Passanger small_pass;
    small_pass.FIO = FIO_in;
    small_pass.age = age_in;
    small_pass.package = package_in;
    return small_pass;
}
// функция регистрации пассажира ( добавлении билета )
Ticket RegisterPassanger(Passanger pass, int number, int in)
{
    // создаем новй экземпляр билета и записываем все данные
    Ticket small_ticket;
    small_ticket.FIO = pass.FIO;
    small_ticket.number = number;
    small_ticket.in = in;
    small_ticket.out = "Санкт-Петербург";
    small_ticket.reg = true;
    small_ticket.unix_date = time(NULL);
    pass.number = number;
    return small_ticket;
}
// функция вывода всей нужной информации о билете пассажира
void ShowFullTicketInfoBuNumber(int numb, vector <Ticket> tickets, int size)
{
    // проверяем циклом зарегистрирован ли такой билет
    int res = -1;
    for (int i = 0; i < size; i++)
    {
        if (tickets[i].number == numb)
        {
            res = i;
            break;
        }
    }
    // если не зарегистрирован, то тогда останавливаем функцию
    if (res == -1) {
        return;
    }
    // в ином случае выводим всю информацию
    cout << "Номер билета : " << tickets[res].number << endl;
    cout << "Дата создания билета : " << tickets[res].unix_date << endl;
    cout << "Город прибытия : " << tickets[res].out << endl;
    cout << "Город отбытия : " << in_cities[tickets[res].in] << endl;
    cout << "Регистрация : " << tickets[res].reg << endl;
    cout << "Посадка : " << tickets[res].checkup << endl;
    cout << "ФИО : " << tickets[res].FIO << endl;
    system("pause");
}
// функция просмотра информации по всем билетам
void CheckTickets(vector <Ticket> tickets, int size)
{
    // создаем 2 вектора
    vector <int> small_index1, small_index2;
    for (int i = 0; i < size; i++)
    {
        // если в билете установлена посадка, тогда добавляем его в первых вектор
        if (tickets[i].checkup == true) small_index1.push_back(i);
        // в ином случае добавляем во второй вектор
        else small_index2.push_back(i);
    }
    cout << "Севшие пасажиры : " << endl;
    // выводим первый вектор, в котром были севшие пассажиры
    for (auto it = small_index1.begin(); it != small_index1.end(); it++)
    {
        cout << "#" << tickets[*it].number << " " << tickets[*it].FIO << endl;
    }
    cout << "Зарегистрированные пасажиры : ";
    // выводим второй вектор, в котором были не севший, но зарегестрированные пассажиры.
    for (auto it = small_index2.begin(); it != small_index2.end(); it++)
    {
        cout << "#" << tickets[*it].number << " " << tickets[*it].FIO << endl;
    }
    // даем возможность узнать подробную информацию о зарегестированном билете
    cout << "Введите номер билета, который хотите осмотреть :";
    int buff;
    cin >> buff;
    ShowFullTicketInfoBuNumber(buff, tickets, size);
}
// ручная функция добавления нового пассажир
Passanger AddPassangerMannualy()
{
    Passanger small_pass;
    int inp;
    string str;
    cout << "Введите ФИО : ";
    cin >> str;
    small_pass.FIO = str;
    cout << "Введите возраст : ";
    cin >> inp;
    small_pass.age = inp;
    cout << "Пассажир с багажом ? 1- да 2- нет : ";
    cin >> inp;
    if (inp == 1)
    {
        small_pass.package = true;
    }
    else small_pass.package = false;
    return small_pass;

}
// вывод информации о пассажире
void ShowInfoForPassanger(Passanger pass)
{
    cout << "ФИО: " << pass.FIO << endl;
    cout << "Возраст: " << pass.age << endl;
    cout << "С багажом? : " << pass.package << endl;
    cout << "Билет #" << pass.number << endl;
    return;
}
int main()
{
    setlocale(LC_ALL, "");
    srand(time(NULL));
    // создаем 2 ветктора 1 с пассажирами другой с билетами
    vector <Passanger> passangers;
    vector <Ticket> tickets;
    // добавляем туда первых трех пассажиров
    passangers.push_back(AddPassanger("Анна Петровна", 48, true));
    passangers.push_back(AddPassanger("Игорь Святославович", 35));
    passangers.push_back(AddPassanger("Андрей Боголюбов", 22));
    // регистрируем этих трех пассаижров
    for (int i = 0; i < passangers.size(); i++)
    {
        int num = tickets.size();
        tickets.push_back(RegisterPassanger(passangers[i], num, rand() % 3));
        passangers[i].number = num;
    }
    // создаем очередь и добавляем туда всех пассажиров
    queue <int> check_queue;
    check_queue.push(0);
    check_queue.push(1);
    check_queue.push(2);

    // вечный цикл программы
    while (true)
    {
        cout << "Введите номер функции" << endl;
        cout << "1 - Продвинуть пассажира в очереди." << endl;
        cout << "2 - Посмотреть всю информацию о билетах." << endl;
        cout << "3 - Добавить пассажира." << endl;
        int inp;
        cin >> inp;
        switch (inp)
        {
        case 1:
        {
            // проверяем не закончилась ли очередь
            if (check_queue.size() <= 1) {
                cout << "Очередь закончена" << "\n";
                continue;
            }
            // выводим 1 пассажира из очереди
            int next_pass = check_queue.front();
            ShowInfoForPassanger(passangers[next_pass]);
            cout << "Посадить пассажира? - 1 " << endl;
            cout << "Выгнать пасажира из очереди? - 2" << endl;
            cout << "Выйти? - 0" << endl;
            int buff;
            cin >> buff;
            if (buff == 1)
            {
                // сажаем пассажира в самолет
                tickets[passangers[next_pass].number].checkup = true;
                check_queue.pop();
            }
            if (buff == 2)
            {
                // убираем пассаижра с регистрации
                tickets[passangers[next_pass].number].reg = false;
                check_queue.pop();
            }
            break;
        }
        case 2: {
            // просмтор информации о билетах
            CheckTickets(tickets, tickets.size());
            break;
        }
        case 3: {
            // добавляем нового пассажира вручную
            int num = passangers.size();
            passangers.push_back(AddPassangerMannualy());
            check_queue.push(num);
            tickets.push_back(RegisterPassanger(passangers[num], num, rand() % 3));
            passangers[num].number = tickets.size() - 1;
        }
        }
    }


}