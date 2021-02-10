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
    cout << " Среднее арифмитическое первой диагонали : " << sum1 << "\n";

    int sum2 = 0;
    for (int i = 9; i >= 0; --i) {
        int j = -(i - 9);
        sum2 += matrix[i][j];
    }
    sum2 = sum2 / 10;
    cout << " Среднее арифимитическое второй диагонали : " << sum2 << "\n";
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
	
    srand(time(NULL)); // обновить последовательность случайных чисел

    int size = 10;
    int** M; // матрица 10 на 10
    M = new int* [size];
    for (int i = 0; i < size; i++)
        M[i] = new int[size];

    for (int i = 0; i < size; i++) // заполняем случайными цифрами матрицу до 99 включительно
        for (int n = 0; n < size; n++)
            M[i][n] = rand() % 100;

    cout << "Сгенерирована случайная матрица 10х10 с числами до 100\n";

    showM(M);

    bool cont = true;
    while (cont) {
        int operation;
        cout << "Введите операцию, которую хотите выполнить ( 1 - транспоририрование матрицы , 2 - среднее арифметическое диагоналей матрицы , 3 - заменить числа на границе их квадратами ) : ";
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
        cout << "Желаете продолжить ( 1 - да, 0 - нет)";
        cin >> x;
        if (x != 1) {
            cont = false;
        }
    }


    system("pause");

}