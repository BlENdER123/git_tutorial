// ���������� ����� 219/5

#include <iostream>
using namespace std;

// ������� ��� ������ ������� �� ����� ��������� 2 ��������� : (���� �������, ������)
void ShowMatrix(int** matrix, int size[2])
{
    // � ������� �������� ����� ������� ������� �� �����
    for (int i = 0; i < size[0]; i++)
    {
        for (int j = 0; j < size[1]; j++) cout << matrix[i][j] << " ";
        cout << endl;
    }
    cout << "����� ������� \n";
}

// ������� ��� ����������� ������ ��������� 3 ��������� ( ������ �������, ������� �������, ������ )
int** SumMatrix(int** matrix, int** matrix2, int size[2])
{
    // ������� ����� ������� ��� ������ ���������� ��������
    int** res = new int* [size[0]];
    // � ������� �������� ����� ���������� 2 ������� � ���������� ��������� � res
    for (int i = 0; i < size[1]; i++)
    {
        // ������� ������ ��� ������� ����������
        res[i] = new int[size[1]];
        for (int j = 0; j < size[0]; j++)
        {
            res[i][j] = matrix[i][j] + matrix2[i][j];
        }
    }
    // ���������� ���������� ���������
    return res;
}

// ������� ��������� 2 ������ ��������� 3 ��������� ( ������ �������, ������ �������, ������ )
int** SubMatrix(int** matrix, int** matrix2, int size[2])
{
    // ������� ����� ������� ��� ������ ���������� ���������
    int** res = new int* [size[0]];
    // � ������� �������� ����� �������� 2 ������� � ���������� ��������� � res
    for (int i = 0; i < size[1]; i++)
    {
        // ������� ������ ��� ������� ����������
        res[i] = new int[size[1]];
        for (int j = 0; j < size[0]; j++)
        {
            res[i][j] = matrix[i][j] - matrix2[i][j];
        }
    }

    return res;
}

// ������� ������������ 2 ������ ��������� 4 ��������� ( ������ �������, ������ �������, ������ ������ �������, ������ ������ ������� )
int** IncMatrix(int** matrix, int** matrix2, int size[2], int size2[2])
{
    // ������� ����� ������� ��� ������ ���������� ������������ 
    int** res = new int* [size[0]];
    for (int i = 0; i < size[0]; i++)
    {
        // ������� ������ ��� ������� ���������� �� �������� ������ ������� ( ��� ������������ ����������� ������ ������ ������� )
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
    // ������ ��� ������� ������ �������
    int size[2];
    cout << "������� ������ ������� 1 > " << endl;
    cin >> size[0];
    cout << "������� ������ ������� 1 > " << endl;
    cin >> size[1];
    // ������ �������
    int** matrix = new int* [size[0]];
    for (int i = 0; i < size[1]; i++)
    {
        matrix[i] = new int[size[1]];
        for (int j = 0; j < size[0]; j++)
        {
            cout << "������� �������� " << i << " " << j << " > ";
            cin >> matrix[i][j];
        }
    }
    
    // ������ ��� �������� ������ �������
    int size2[2];
    cout << "������� ������ ������� 1 > " << endl;
    cin >> size2[0];
    cout << "������� ������ ������� 1 > " << endl;
    cin >> size2[1];
    // ������ �������
    int** matrix2 = new int* [size2[0]];
    for (int i = 0; i < size2[1]; i++)
    {
        matrix2[i] = new int[size2[1]];
        for (int j = 0; j < size2[0]; j++)
        {
            cout << "������� ��������2 " << i << " " << j << " > ";
            cin >> matrix2[i][j];
        }
    }
    
    // ������� ����
    while (true)
    {
        system("cls");
        // ���������� 2 ��������� ������� ������������
        ShowMatrix(matrix, size);
        ShowMatrix(matrix2, size2);
        cout << "����� ������� ������ ���������" << endl;
        cout << "1. �������� ������(����������� �������)" << endl;
        cout << "2. �������� ������" << endl;
        cout << "3. ��������� ������" << endl;
        int input;
        cin >> input;
        switch (input)
        {
        case 1:
        {
            // ��������� ����� ������ ������ ��� ���������� ( �������� � ��������� ������ �������� ������ ��� ���������� ������� ������ )
            if (size[0] != size2[0] || size[1] != size2[1])
            {
                cout << "������� ������ ���� ����������� �������" << endl;
                break;
            }
            // ����������� ���������� ��������� �������� � ��������� ����������
            int** temp_result = SumMatrix(matrix, matrix2, size);
            // � ������� ���������� ��������� ������������
            ShowMatrix(temp_result, size);
            delete[] temp_result;

            break;
        }
        case 2:
        {
            if (size[0] != size2[0] || size[1] != size2[1])
            {
                cout << "������� ������ ���� ����������� �������" << endl;
                break;
            }
            int** temp_result = SubMatrix(matrix, matrix2, size);
            ShowMatrix(temp_result, size);
            delete[] temp_result;
            break;
        }
        case 3:
        {
            // ��������� ����� ������ ������� ��������� � ������� ( ������������ ������� �������� ������, ���� ������ ������ ������ ��������� � ������� ������ ������� )
            if (size[1] != size2[0])
            {
                cout << "���������� �������� ������� 1 ������ ��������� � ����������� ����� ������� 2." << endl;
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