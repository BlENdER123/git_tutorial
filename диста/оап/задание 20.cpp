// Задорожний Антон 219/5
#include <iostream>
#include <string>
//#include <time.h>
#include <queue>
#include <vector>
#include <conio.h>
using namespace std;

void showM(int** M) {
    for (int i = 0; i < 3; i++)
    {
        for (int n = 0; n < 3; n++) {
            cout.width(2);
            std::cout << M[i][n] << " ";
        }
        cout << "\n";
    }
}

int opred(int** matrix1) {
    int opred = (matrix1[0][0] * matrix1[1][1] * matrix1[2][2]) + (matrix1[0][2] * matrix1[1][0] * matrix1[2][1]) + (matrix1[2][0] * matrix1[0][1] * matrix1[1][2]) - (matrix1[2][0] * matrix1[1][1] * matrix1[0][2]) - (matrix1[0][0] * matrix1[2][1] * matrix1[1][2]) - (matrix1[2][2] * matrix1[1][0] * matrix1[0][1]);

    return opred;
}

int delta_opred(int** matrix,int stolb, int matrix2[3][1]) {

    const int size = 3;

    int** temp;
    temp = new int* [size];
    for (int i = 0; i < size; i++) {
        temp[i] = new int[size];
    }

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            temp[i][j] = matrix[i][j];
        }
    }

    for (int i = 0; i < size; i++) {
        temp[i][stolb] = matrix2[i][0];
    }

    showM(temp);

    int temp_opred = opred(temp);

    cout << "определитель x" << stolb+1 << " уравнения = " << temp_opred << "\n";

    cout << "*************** \n";


    return temp_opred;
}

int main()
{
    setlocale(LC_ALL, "Russian");
    srand(time(NULL));

    const int size = 3;

    int** matrix1;
    matrix1 = new int* [size];
    for (int i = 0; i < size; i++) {
        matrix1[i] = new int[size];
    }

    int matrix2[size][1];

    while (true) {
        system("cls");
        cout << "Введите 1 - чтобы решить матрицу методом Крамера 0 - чтобы выйти : ";
        bool res;
        cin >> res;

        if (res) {

            for (int i = 0; i < 3; i++) {
                cout << "Введите систему уравнений типо x1+x2+x3=z \n";
                cout << "Введите x1 : ";
                int x1;
                cin >> x1;
                cout << "\n";
                cout << "Введите x2 : ";
                int x2;
                cin >> x2;
                cout << "\n";
                cout << "Введите x3 : ";
                int x3;
                cin >> x3;
                cout << "\n";
                cout << "Введите z : ";
                int z;
                cin >> z;

                matrix1[i][0] = x1;
                matrix1[i][1] = x2;
                matrix1[i][2] = x3;
                matrix2[i][0] = z;
            }

            cout << "Изначальная матрица : \n";

            showM(matrix1);

            cout << "*************** \n";


            int opred_main = opred(matrix1);
            if (opred_main == 0) {
                cout << "Определитель данной матрицы равен 0, метод Крамера не подходит \n";
                system("pause");
                continue;
            }

            int opred_x1 = delta_opred(matrix1, 0, matrix2);

            int opred_x2 = delta_opred(matrix1, 1, matrix2);

            int opred_x3 = delta_opred(matrix1, 2, matrix2);

            cout << "Находим решения уравнения \n";

            cout << "x1 = " << opred_x1 / opred_main << "\n";
            cout << "x2 = " << opred_x2 / opred_main << "\n";
            cout << "x3 = " << opred_x3 / opred_main << "\n";
            cout << "\n";
            system("pause");
        }
        else {
            exit;
        }

        

    }
}