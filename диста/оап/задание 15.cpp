#include <iostream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

set <int> set_show(set <int> s) {
	for (auto i = s.begin(); i != s.end(); i++) {
		cout << *i << " ";
	}
	return s;
}

vector <int> vector_show(vector <int> v) {
	for (auto i = v.begin(); i != v.end(); i++) {
		cout << *i << " ";
	}
	return v;
}

vector<int> VectorIntersection(vector<int> x1, vector<int> x2)
{
	vector<int> x3;
	set_intersection(x1.begin(), x1.end(), x2.begin(), x2.end(), back_inserter(x3));

	return x3;
}

vector<int> VectorDifference(vector<int> x1, vector<int> x2)
{
	vector<int> x3;
	set_difference(x1.begin(), x1.end(), x2.begin(), x2.end(), back_inserter(x3));
	return x3;
}

vector<int> VectorSDifference(vector<int> x1, vector<int> x2)
{
	vector<int> x3;
	set_symmetric_difference(x1.begin(), x1.end(), x2.begin(), x2.end(), back_inserter(x3));
	return x3;
}

vector<int> VectorUnion(vector<int> x1, vector<int> x2)
{
	vector<int> x3;
	set_union(x1.begin(), x1.end(), x2.begin(), x2.end(), back_inserter(x3));
	return x3;
}


set<int> SetIntersection(set<int> x1, set<int> x2)
{
	set<int> x3;
	set_intersection(x1.begin(), x1.end(), x2.begin(), x2.end(), inserter(x3, x3.end()));
	return x3;
}

set<int> SetDifference(set<int> x1, set<int> x2)
{
	set<int> x3;
	set_difference(x1.begin(), x1.end(), x2.begin(), x2.end(), inserter(x3, x3.end()));
	return x3;
}

set<int> SetSDifference(set<int> x1, set<int> x2)
{
	set<int> x3;
	set_symmetric_difference(x1.begin(), x1.end(), x2.begin(), x2.end(), inserter(x3, x3.end()));
	return x3;
}

set<int> SetUnion(set<int> x1, set<int> x2)
{
	set <int> x3;
	set_union(x1.begin(), x1.end(), x2.begin(), x2.end(), inserter(x3, x3.end()));
	return x3;
}



int main() {
	setlocale(LC_ALL, "Russian");
	vector <int> v1;
	vector <int> v2;
	vector <int> v3;

	set <int> s1;
	set <int> s2;
	set <int> s3;

	bool check = true;

	while (check)
	{

		string type;
		cout << "Выберите : 1 - вектор, 2 - сет" << endl;
		cin >> type;

		if (type == "2") {

			int x;
			cout << "Сколько элементов будет в первом сете? " << endl;
			cin >> x;

			cout << "Введите элементы первого сета" << endl;
			for (int c = 0; c < x; c++)
			{
				int i;
				cin >> i;
				s1.insert(i);
			}

			cout << "Сколько элементов будет вo втором сете? ";
			cin >> x;
			cout << "Введите элементы второго сета";
			for (int c = 0; c < x; c++)
			{
				int i;
				cin >> i;
				s2.insert(i);
			}
			char op;
			cout << "Выберите функцию: 1-set_intersection, 2 - set_difference, 3 - set_symmetric_difference, 4 - set_union" << endl;
			cin >> op;
			if (op == '1')
			{
				s3 = SetIntersection(s1, s2);
				set_show(s3);
			}
			if (op == '2') {
				s3 = SetDifference(s1, s2);
				set_show(s3);
			}
			if (op == '3') {
				s3 = SetSDifference(s1, s2);
				set_show(s3);
			}
			if (op == '4') {
				s3 = SetUnion(s1, s2);
				set_show(s3);
			}
			int cont;
			cout << "Хотите продолжить? (1-Да, 2-Нет) " << endl;
			cin >> cont;
			if (cont == 1) {
				check = true;
			}
			if (cont == 2) {
				check = false;
			}

		}

		if (type == "1") {

			int x;
			cout << "Сколько элементов будет в первом векторе? " << endl;
			cin >> x;

			cout << "Введите элементы первого вектора" << endl;
			for (int c = 0; c < x; c++)
			{
				int i;
				cin >> i;
				v1.push_back(i);
			}

			cout << "Сколько элементов будет вo втором векторе? ";
			cin >> x;
			cout << "Введите элементы второго вектора: ";
			for (int c = 0; c < x; c++)
			{
				int i;
				cin >> i;
				v2.push_back(i);
			}
			char op;
			cout << "Выберите функцию: 1-set_intersection, 2 - set_difference, 3 - set_symmetric_difference, 4 - set_union" << endl;
			cin >> op;
			if (op == '1')
			{
				v3 = VectorIntersection(v1, v2);
				vector_show(v3);
			}
			if (op == '2') {
				v3 = VectorDifference(v1, v2);
				vector_show(v3);
			}
			if (op == '3') {
				v3 = VectorSDifference(v1, v2);
				vector_show(v3);
			}
			if (op == '4') {
				v3 = VectorUnion(v1, v2);
				vector_show(v3);
			}
			int cont;
			cout << "Хотите продолжить? (1-Да, 2-Нет) " << endl;
			cin >> cont;
			if (cont == 1) {
				check = true;
			}
			if (cont == 2) {
				check = false;
			}

		}

	}
}