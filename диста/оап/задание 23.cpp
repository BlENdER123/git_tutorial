#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>
#include <vector>

using namespace std;

// ������� ��� ������ ����� � ���������
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

// ������� ��� ������ ������� � �������
void show_fams(vector <string> data)
{
    for (auto it = data.begin(); it != data.end(); it++) {
        cout << "������� : " << *it << endl;
    }
}

// ������� ��� ������ ������� � �����
void search_fams(vector <string> data, string search_data) {
    bool success = false;
    for (int i = 0; i < data.size(); i++) {

        if (search_data == data[i]) {
            cout << "��������� �������: " << data[i] << " � �������  " << i+1 << endl;
            success = true;
        }
    }
    if (!success) cout << "������� �� �������." << endl;
}


int main() {

    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    cout << "������� �������� ����� " << endl;
    string file_name;
    cin >> file_name;

    while (true)
    {
        cout << "�������� ������� ��� ������ � ������ " << endl;
        cout << "1) �������� ������� � ����" << endl;
        cout << "2) �������� ������� � �����" << endl;
        cout << "3) ����� ������� �� ����� �����" << endl;

        int res;
        cin >> res;
        
        if (res == 1) {

            cout << "������� ����� �������: ";
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

            cout << "������� ������� �������  ";
            string familia;
            cin >> familia;

            search_fams(read_fams(file_name + ".txt"), familia);

        }
        else {

            cout << "��������� ������� �� �������";

        }

    }
    return 0;
}