#include<fstream>
#include<iostream>
#include<locale>
#include<vector>
#include<set>
#include<Windows.h>
#include<iterator>
#include<string>

using namespace std;

int main() {
	setlocale(LC_ALL, "Russian");
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);

	ifstream out, out1;

	set<string> list;
	vector<string> vec;
	string buffer;

	cout << "������� ��� �����, ������� ������ �������?(������: Example.txt)" << endl;
	string name;
	cin >> name;

	do{
		out.open(name, ios::app);
		if (!out.is_open()) {
			cout << "������ �������� �����, ��������� ����!" << endl;
			cin >> name;
		}
	} while (!out.is_open());
	
	while (out) {
		getline(out, buffer);
		if (buffer != " ") {
			vec.push_back(buffer);
		}
		buffer = " ";
	}
	out.close();

	out.open(name, ios::app);
	while (out) {
		getline(out, buffer);
		if (buffer != " ") {
			list.insert(buffer);
		}
		buffer = " ";
	}
	out.close();

	if (vec.size() != list.size()) {
		cout << "� ����� ���� ������������� ��������" << endl << "������ ��������� vector:" << endl;
		for (int i = 0; i < vec.size(); i++) {
			cout << vec[i] << endl;
		}
	}
	else {
		cout << "� ����� ��� �������� ���������." << endl << "������ ��������� set:" << endl;
		for (auto iter = list.begin(); iter != list.end(); ++iter) {
			cout << *iter << endl;
		}
	}
	system("pause");
}
