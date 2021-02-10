// Задорожний Антон 219/5

#include <iostream>
using namespace std;

// функция для вывода матрицы на экран принимает 2 аргумента : (саму матрицу, размер)
void ShowMatrix(int** matrix, int size[2])
{
    // с помощью двойного цикла выводим матрицу на экран
    for (int i = 0; i < size[0]; i++)
    {
        for (int j = 0; j < size[1]; j++) cout << matrix[i][j] << " ";
        cout << endl;
    }
    cout << "Конец матрицы \n";
}

// функция для складывания матриц принимает 3 аргумента ( первую матрицу, всторую матрицу, размер )
int** SumMatrix(int** matrix, int** matrix2, int size[2])
{
    // создаем новую матрицу для записи результата сложения
    int** res = new int* [size[0]];
    // с помощью двойного цикла складываем 2 матрицы и записываем результат в res
    for (int i = 0; i < size[1]; i++)
    {
        // создаем строки для матрицы результата
        res[i] = new int[size[1]];
        for (int j = 0; j < size[0]; j++)
        {
            res[i][j] = matrix[i][j] + matrix2[i][j];
        }
    }
    // возвращаем полученный результат
    return res;
}

// функция вычитания 2 матриц принимает 3 аргумента ( первую матрицу, вторую мартицу, размер )
int** SubMatrix(int** matrix, int** matrix2, int size[2])
{
    // создаем новую матрицу для записи результата вычитания
    int** res = new int* [size[0]];
    // с помощью двойного цикла вычитаем 2 матрицы и записываем результат в res
    for (int i = 0; i < size[1]; i++)
    {
        // создаем строки для матрицы результата
        res[i] = new int[size[1]];
        for (int j = 0; j < size[0]; j++)
        {
            res[i][j] = matrix[i][j] - matrix2[i][j];
        }
    }

    return res;
}

// функция произведения 2 матриц принимает 4 аргумента ( первую матрицу, вторую матрицу, размер первой матрицы, размер второй мартицы )
int** IncMatrix(int** matrix, int** matrix2, int size[2], int size2[2])
{
    // создаем новую матрицу для записи результата произведения 
    int** res = new int* [size[0]];
    for (int i = 0; i < size[0]; i++)
    {
        // создаем строки для матрицы результата из размеров второй матрицы ( при произведении сохраняется размер второй матрицы )
        res[i] = new int[size2[1]];
        for (int j = 0; j < size2[1]; j++)
        {
            res[i][j] = 0;
            for (int k = 0; k < size[1]; k++)
                res[i][j] += matrix[i][k] * matrix2[k][j];
        }
    }
    return res;
}

int main()
{
    setlocale(LC_ALL, "");
    // массив для размера первой матрицы
    int size[2];
    cout << "Введите ширину матрицы 1 > " << endl;
    cin >> size[0];
    cout << "Введите высоту матрицы 1 > " << endl;
    cin >> size[1];
    // первая матрицы
    int** matrix = new int* [size[0]];
    for (int i = 0; i < size[1]; i++)
    {
        matrix[i] = new int[size[1]];
        for (int j = 0; j < size[0]; j++)
        {
            cout << "Введите значение " << i << " " << j << " > ";
            cin >> matrix[i][j];
        }
    }
    
    // массив для размеров второй матрицы
    int size2[2];
    cout << "Введите ширину матрицы 1 > " << endl;
    cin >> size2[0];
    cout << "Введите высоту матрицы 1 > " << endl;
    cin >> size2[1];
    // вторая матрицы
    int** matrix2 = new int* [size2[0]];
    for (int i = 0; i < size2[1]; i++)
    {
        matrix2[i] = new int[size2[1]];
        for (int j = 0; j < size2[0]; j++)
        {
            cout << "Введите значение2 " << i << " " << j << " > ";
            cin >> matrix2[i][j];
        }
    }
    
    // рабочий цикл
    while (true)
    {
        system("cls");
        // показываем 2 введенных матрицы пользователю
        ShowMatrix(matrix, size);
        ShowMatrix(matrix2, size2);
        cout << "Выбор функции работы программы" << endl;
        cout << "1. Сложение матриц(одинакового размера)" << endl;
        cout << "2. Разность матриц" << endl;
        cout << "3. Умножение матриц" << endl;
        int input;
        cin >> input;
        switch (input)
        {
        case 1:
        {
            // проверяем чтобы размер матриц был одинаковый ( сложение и вычитание матриц возможно только при одиноковом размере матриц )
            if (size[0] != size2[0] || size[1] != size2[1])
            {
                cout << "Матрицы должны быть одинакового размера" << endl;
                break;
            }
            // присваиваем полученный результат сложения к временной переменной
            int** temp_result = SumMatrix(matrix, matrix2, size);
            // и выводим полученный результат пользователю
            ShowMatrix(temp_result, size);
            delete[] temp_result;

            break;
        }
        case 2:
        {
            if (size[0] != size2[0] || size[1] != size2[1])
            {
                cout << "Матрицы должны быть одинакового размера" << endl;
                break;
            }
            int** temp_result = SubMatrix(matrix, matrix2, size);
            ShowMatrix(temp_result, size);
            delete[] temp_result;
            break;
        }
        case 3:
        {
            // проверяем чтобы ширина матрицы совпадала с высотой ( произведение матрицы возможно только, если ширина первой мартцы совпадает с высотой второй матрицы )
            if (size[1] != size2[0])
            {
                cout << "Количество столбцов матрицы 1 должно совпадать с количеством строк матрицы 2." << endl;
                break;
            }
            int** temp_result = IncMatrix(matrix, matrix2, size, size2);
            ShowMatrix(temp_result, size);
            delete[] temp_result;
            break;

        }
        }
        system("pause");
    }
}