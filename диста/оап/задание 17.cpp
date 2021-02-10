#include <iostream>
#include <iterator>
#include <algorithm>
#include <stack>
#include <queue>

using namespace std;

void steck() {
    stack <int> steck;  // ������� ����

    int i = 0;

    cout << "������� ���� ����� ����� �����: " << endl;
    while (i != 5) {
        int a;
        cin >> a;
        steck.push(a);  // ��������� ��������� �����
        i++;
    }

    while (steck.size() != 1) {
        cout << "������� ������� �����: " << steck.top() << endl; // ������� ������� �������
        cout << "������� ������ ������� ������� " << endl;
        steck.pop();  // ������� ������� �������
        cout << "� ��� ����� ������� �������: " << steck.top() << "\n";
    }

    cout << "stack ����������";
}

void qu() {
    queue <int> q;  // ������� ������� queue

    cout << "������������, ���������� ������� 5 �����: " << endl;

    for (int h = 0; h < 5; h++) {
        int a;
        cin >> a;
        q.push(a);
    }

    while (q.size() != 1) {
        cout << "����� ������ ������� � �������: " << q.front() << endl;
        q.pop();  // ������� ������� �� �������
        cout << "����� ������ ������� (����� ��������): " << q.front() << endl;
    }

    cout << "queue ����������";

}

int main() {
	setlocale(LC_ALL, "Russian");
	
    steck();
    qu();

    system("pause");

}