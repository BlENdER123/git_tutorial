// ���������� ����� 219/5
#include <iostream>
#include <string>
#include <time.h>
#include <queue>
#include <vector>
using namespace std;

// ������ � ���������� �������� ��������
string in_cities[] = { "������", "�����","����" };

// ��������� ��������� � ��������, ����� �����, ���������, � �������.
struct Passanger {
    string FIO;
    int number;
    int age;
    bool package;
};
// ��������� ������ � ������� �����, ����� �������� ������, ������� ��������, ������� �������, ������������, �������� � ���.
struct Ticket {
    int number;
    time_t unix_date;
    string out;
    int in;
    bool reg;
    bool checkup;
    string FIO;
};
// ������� ������� ���������� ������ ���������
Passanger AddPassanger(string FIO_in, int age_in, bool package_in = false)
{
    // ������� ����� ��������� ��������� � ���������� ��� ���������� ������
    Passanger small_pass;
    small_pass.FIO = FIO_in;
    small_pass.age = age_in;
    small_pass.package = package_in;
    return small_pass;
}
// ������� ����������� ��������� ( ���������� ������ )
Ticket RegisterPassanger(Passanger pass, int number, int in)
{
    // ������� ���� ��������� ������ � ���������� ��� ������
    Ticket small_ticket;
    small_ticket.FIO = pass.FIO;
    small_ticket.number = number;
    small_ticket.in = in;
    small_ticket.out = "�����-���������";
    small_ticket.reg = true;
    small_ticket.unix_date = time(NULL);
    pass.number = number;
    return small_ticket;
}
// ������� ������ ���� ������ ���������� � ������ ���������
void ShowFullTicketInfoBuNumber(int numb, vector <Ticket> tickets, int size)
{
    // ��������� ������ ��������������� �� ����� �����
    int res = -1;
    for (int i = 0; i < size; i++)
    {
        if (tickets[i].number == numb)
        {
            res = i;
            break;
        }
    }
    // ���� �� ���������������, �� ����� ������������� �������
    if (res == -1) {
        return;
    }
    // � ���� ������ ������� ��� ����������
    cout << "����� ������ : " << tickets[res].number << endl;
    cout << "���� �������� ������ : " << tickets[res].unix_date << endl;
    cout << "����� �������� : " << tickets[res].out << endl;
    cout << "����� ������� : " << in_cities[tickets[res].in] << endl;
    cout << "����������� : " << tickets[res].reg << endl;
    cout << "������� : " << tickets[res].checkup << endl;
    cout << "��� : " << tickets[res].FIO << endl;
    system("pause");
}
// ������� ��������� ���������� �� ���� �������
void CheckTickets(vector <Ticket> tickets, int size)
{
    // ������� 2 �������
    vector <int> small_index1, small_index2;
    for (int i = 0; i < size; i++)
    {
        // ���� � ������ ����������� �������, ����� ��������� ��� � ������ ������
        if (tickets[i].checkup == true) small_index1.push_back(i);
        // � ���� ������ ��������� �� ������ ������
        else small_index2.push_back(i);
    }
    cout << "������ �������� : " << endl;
    // ������� ������ ������, � ������ ���� ������ ���������
    for (auto it = small_index1.begin(); it != small_index1.end(); it++)
    {
        cout << "#" << tickets[*it].number << " " << tickets[*it].FIO << endl;
    }
    cout << "������������������ �������� : ";
    // ������� ������ ������, � ������� ���� �� ������, �� ������������������ ���������.
    for (auto it = small_index2.begin(); it != small_index2.end(); it++)
    {
        cout << "#" << tickets[*it].number << " " << tickets[*it].FIO << endl;
    }
    // ���� ����������� ������ ��������� ���������� � ����������������� ������
    cout << "������� ����� ������, ������� ������ ��������� :";
    int buff;
    cin >> buff;
    ShowFullTicketInfoBuNumber(buff, tickets, size);
}
// ������ ������� ���������� ������ ��������
Passanger AddPassangerMannualy()
{
    Passanger small_pass;
    int inp;
    string str;
    cout << "������� ��� : ";
    cin >> str;
    small_pass.FIO = str;
    cout << "������� ������� : ";
    cin >> inp;
    small_pass.age = inp;
    cout << "�������� � ������� ? 1- �� 2- ��� : ";
    cin >> inp;
    if (inp == 1)
    {
        small_pass.package = true;
    }
    else small_pass.package = false;
    return small_pass;

}
// ����� ���������� � ���������
void ShowInfoForPassanger(Passanger pass)
{
    cout << "���: " << pass.FIO << endl;
    cout << "�������: " << pass.age << endl;
    cout << "� �������? : " << pass.package << endl;
    cout << "����� #" << pass.number << endl;
    return;
}
int main()
{
    setlocale(LC_ALL, "");
    srand(time(NULL));
    // ������� 2 �������� 1 � ����������� ������ � ��������
    vector <Passanger> passangers;
    vector <Ticket> tickets;
    // ��������� ���� ������ ���� ����������
    passangers.push_back(AddPassanger("���� ��������", 48, true));
    passangers.push_back(AddPassanger("����� �������������", 35));
    passangers.push_back(AddPassanger("������ ���������", 22));
    // ������������ ���� ���� ����������
    for (int i = 0; i < passangers.size(); i++)
    {
        int num = tickets.size();
        tickets.push_back(RegisterPassanger(passangers[i], num, rand() % 3));
        passangers[i].number = num;
    }
    // ������� ������� � ��������� ���� ���� ����������
    queue <int> check_queue;
    check_queue.push(0);
    check_queue.push(1);
    check_queue.push(2);

    // ������ ���� ���������
    while (true)
    {
        cout << "������� ����� �������" << endl;
        cout << "1 - ���������� ��������� � �������." << endl;
        cout << "2 - ���������� ��� ���������� � �������." << endl;
        cout << "3 - �������� ���������." << endl;
        int inp;
        cin >> inp;
        switch (inp)
        {
        case 1:
        {
            // ��������� �� ����������� �� �������
            if (check_queue.size() <= 1) {
                cout << "������� ���������" << "\n";
                continue;
            }
            // ������� 1 ��������� �� �������
            int next_pass = check_queue.front();
            ShowInfoForPassanger(passangers[next_pass]);
            cout << "�������� ���������? - 1 " << endl;
            cout << "������� �������� �� �������? - 2" << endl;
            cout << "�����? - 0" << endl;
            int buff;
            cin >> buff;
            if (buff == 1)
            {
                // ������ ��������� � �������
                tickets[passangers[next_pass].number].checkup = true;
                check_queue.pop();
            }
            if (buff == 2)
            {
                // ������� ��������� � �����������
                tickets[passangers[next_pass].number].reg = false;
                check_queue.pop();
            }
            break;
        }
        case 2: {
            // �������� ���������� � �������
            CheckTickets(tickets, tickets.size());
            break;
        }
        case 3: {
            // ��������� ������ ��������� �������
            int num = passangers.size();
            passangers.push_back(AddPassangerMannualy());
            check_queue.push(num);
            tickets.push_back(RegisterPassanger(passangers[num], num, rand() % 3));
            passangers[num].number = tickets.size() - 1;
        }
        }
    }


}