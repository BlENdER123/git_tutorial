#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>
#include <vector>

using namespace std;

// функция для чтения файла с фамилиями
vector <string> read_fams(string filename)
{
    ifstream read(filename);
    vector <string> data;
    if (read.is_open())
    {
        while (read)
        {
            string text;
            getline(read, text);
            if (text.empty()) break;
            data.push_back(text);

        }
    }
    return data;
}

// функция для вывода фамилий в консоль
void show_fams(vector <string> data)
{
    for (auto it = data.begin(); it != data.end(); it++) {
        cout << "Фамилия : " << *it << endl;
    }
}

// функция для поиска фамилий в файле
void search_fams(vector <string> data, string search_data) {
    bool success = false;
    for (int i = 0; i < data.size(); i++) {

        if (search_data == data[i]) {
            cout << "Найденная фамилия: " << data[i] << " с номером  " << i+1 << endl;
            success = true;
        }
    }
    if (!success) cout << "Фамилия не найдена." << endl;
}


int main() {

    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    cout << "Введите название файла " << endl;
    string file_name;
    cin >> file_name;

    while (true)
    {
        cout << "Выберите функцию для работы с файлом " << endl;
        cout << "1) Добавить фамилию в файл" << endl;
        cout << "2) Показать фамилию в файле" << endl;
        cout << "3) Поиск фамилии по всему файлу" << endl;

        int res;
        cin >> res;
        
        if (res == 1) {

            cout << "Введите новую фамилию: ";
            string familia;
            cin >> familia;

            ofstream write(file_name + ".txt", ios::app);
            write << familia << "\n";
            write.close();

        }
        else if (res == 2) {

            show_fams(read_fams(file_name + ".txt"));

        }
        else if (res == 3) {

            cout << "Введите искомую фамилию  ";
            string familia;
            cin >> familia;

            search_fams(read_fams(file_name + ".txt"), familia);

        }
        else {

            cout << "Выбранная функция не найдена";

        }

    }
    return 0;
}