// Задорожний Антон 219/5
#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <Windows.h>
using namespace std;

void read_file(string filename)
{
    ifstream rd(filename);
    while (rd)
    {
        string date;
        string text;
        getline(rd, date, '|');
        if (date.empty()) break;
        cout << "Дата: " << date;
        getline(rd, text);
        cout << "Текст: " << text << endl;
    }

}
int main() {
    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    while (true)
    {
        cout << "Выбор функции :" << endl;
        cout << "1.Добавить заметку" << endl;
        cout << "2.Прочитать все заметки" << endl;
        int inp;
        cin >> inp;
        if (inp == 1)
        {
            string text;
            cout << "Введите текст: ";
            cin >> text;
            ofstream write("book.txt", ios::app);
            time_t t;
            time(&t);
            char str[80];
            ctime_s(str, sizeof(str), &t);
            write << str << "|" << text << "\n";
            write.close();
        }
        else if (inp == 2)
        {
            read_file("book.txt");
        }
        else break;
    }
    return 0;
}