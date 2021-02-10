#include <iostream>
#include <iterator>
#include <algorithm>
#include <stack>
#include <queue>

using namespace std;

void steck() {
    stack <int> steck;  // создаем стек

    int i = 0;

    cout << "Введите пять любых целых чисел: " << endl;
    while (i != 5) {
        int a;
        cin >> a;
        steck.push(a);  // добавляем введенные числа
        i++;
    }

    while (steck.size() != 1) {
        cout << "Верхний элемент стека: " << steck.top() << endl; // выводим верхний элемент
        cout << "Давайте удалим верхний элемент " << endl;
        steck.pop();  // удаляем верхний элемент
        cout << "А это новый верхний элемент: " << steck.top() << "\n";
    }

    cout << "stack закончился";
}

void qu() {
    queue <int> q;  // создали очередь queue

    cout << "Пользователь, пожалуйста введите 5 чисел: " << endl;

    for (int h = 0; h < 5; h++) {
        int a;
        cin >> a;
        q.push(a);
    }

    while (q.size() != 1) {
        cout << "Самый первый элемент в очереди: " << q.front() << endl;
        q.pop();  // удаляем элемент из очереди
        cout << "Новый первый элемент (после удаления): " << q.front() << endl;
    }

    cout << "queue закончился";

}

int main() {
	setlocale(LC_ALL, "Russian");
	
    steck();
    qu();

    system("pause");

}