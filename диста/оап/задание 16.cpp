#include <iostream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <set>
#include <ctime> 

using namespace std;

void showM(int **M) {
    for (int i = 0; i < 10; i++)
    {
        for (int n = 0; n < 10; n++) {
            cout.width(2);
            std::cout << M[i][n] << " ";
        }
        cout << "\n";
    }
}

int transpose(int **matrix)
{
    int t;
    for (int i = 0; i < 10; ++i)
    {
        for (int j = i; j < 10; ++j)
        {
            t = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = t;
        }
    }
    return **matrix;
}

void diag(int **matrix) {
    int sum1 = 0;
    for (int i = 0; i < 10; ++i) {
        sum1 += matrix[i][i];
    }
    sum1 = sum1 / 10;
    cout << " ������� �������������� ������ ��������� : " << sum1 << "\n";

    int sum2 = 0;
    for (int i = 9; i >= 0; --i) {
        int j = -(i - 9);
        sum2 += matrix[i][j];
    }
    sum2 = sum2 / 10;
    cout << " ������� ��������������� ������ ��������� : " << sum2 << "\n";
}

int kvadrat(int** matrix) {

    for (int i = 1; i < 9; i++) {
        matrix[i][0] = matrix[i][0] * matrix[i][0];
    }
    for (int i = 1; i < 9; i++) {
        matrix[i][9] = matrix[i][9] * matrix[i][9];
    }
    for (int i = 1; i < 9; i++) {
        matrix[0][i] = matrix[0][i] * matrix[0][i];
    }
    for (int i = 1; i < 9; i++) {
        matrix[9][i] = matrix[9][i] * matrix[9][i];
    }
    matrix[0][0] = matrix[0][0] * matrix[0][0];
    matrix[9][9] = matrix[9][9] * matrix[9][9];
    matrix[0][9] = matrix[0][9] * matrix[0][9];
    matrix[9][0] = matrix[9][0] * matrix[9][0];

    return **matrix;
}


int main() {
	setlocale(LC_ALL, "Russian");
	
    srand(time(NULL)); // �������� ������������������ ��������� �����

    int size = 10;
    int** M; // ������� 10 �� 10
    M = new int* [size];
    for (int i = 0; i < size; i++)
        M[i] = new int[size];

    for (int i = 0; i < size; i++) // ��������� ���������� ������� ������� �� 99 ������������
        for (int n = 0; n < size; n++)
            M[i][n] = rand() % 100;

    cout << "������������� ��������� ������� 10�10 � ������� �� 100\n";

    showM(M);

    bool cont = true;
    while (cont) {
        int operation;
        cout << "������� ��������, ������� ������ ��������� ( 1 - ������������������ ������� , 2 - ������� �������������� ���������� ������� , 3 - �������� ����� �� ������� �� ���������� ) : ";
        cin >> operation;

        if (operation == 1) {
            **M = transpose(M);
            showM(M);

        }
        if (operation == 2) {
            diag(M);
        }
        if (operation == 3) {
            **M = kvadrat(M);
            showM(M);
        }

        int x;
        cout << "������� ���������� ( 1 - ��, 0 - ���)";
        cin >> x;
        if (x != 1) {
            cont = false;
        }
    }


    system("pause");

}