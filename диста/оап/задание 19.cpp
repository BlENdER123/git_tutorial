// ���������� ����� 219/5
#include <iostream>
#include <string>
#include <time.h>
#include <queue>
#include <vector>
#include <conio.h>
using namespace std;


struct Product {
    int numb;
    string name;
    int quantity;

    string video_card;
    string processor;
    int RAM;
    bool floppy_drive;
};

Product addProduct(int n, string name, int q, string vc, string p, int r, bool f) {
    Product pc;
    pc.numb = n;
    pc.name = name;
    pc.quantity = q;
    pc.video_card = vc;
    pc.processor = p;
    pc.RAM = r;
    pc.floppy_drive = f;

    return pc;
};

void findNumberProduct(vector <Product> p) {

    cout << "������� ��� ������ : ";
    int n;
    cin >> n;

    for (int i = 0; i < p.size(); i++) {
        if (p[i].numb == n) {
            cout << " ��������: " << p[i].name << endl;
            cout << " ���������: " << p[i].processor << endl;
            cout << " ����������� ������: " << p[i].RAM << " GB" << endl;
            cout << " ����������: " << p[i].video_card << endl;
            cout << " �������� : " << p[i].floppy_drive << endl;
            cout << " ���������� ������ : " << p[i].quantity << endl;
            cout << " ��� ��������: " << p[i].numb << endl;
        }
    }
    system("pause");
}

void findWordProduct(vector <Product> p)
{
    string vc;
    cout << "������� ������ ���������� : ";
    cin >> vc;

    cout << "\n";

    string pr;
    cout << "������� ������ ��������� : ";
    cin >> pr;

    cout << "\n";

    int r;
    cout << "������� ������ ���������� ����������� ������ : ";
    cin >> r;

    cout << "\n";

    bool fd;
    cout << "����� �������� (1 - ��, 0 - ���) :  ";
    cin >> fd;

    cout << "\n";

    for (int i = 0; i < p.size(); i++) {
        if ((vc == p[i].video_card) & (pr == p[i].processor) & (r == p[i].RAM) & (fd == p[i].floppy_drive)) {
            cout << " ��������: " << p[i].name << endl;
            cout << " ���������: " << p[i].processor << endl;
            cout << " ����������� ������: " << p[i].RAM << " GB" << endl;
            cout << " ����������: " << p[i].video_card << endl;
            cout << " �������� : " << p[i].floppy_drive << endl;
            cout << " ���������� ������ : " << p[i].quantity << endl;
            cout << " ��� ��������: " << p[i].numb << endl;
            cout << endl;
        }
    }
    system("pause");
}

vector <Product> buyProduct(vector <Product> p) {

    cout << "������� ������ �� (1 - ��, 0 - ���) ? :  ";
    bool buy;
    cin >> buy;

    if (buy) {
        cout << "������� ��� ������ : ";
        int n;
        cin >> n;

        for (int i = 0; i < p.size(); i++) {
            if (n == p[i].numb) {
                cout << " ��������: " << p[i].name << endl;
                cout << " ���������: " << p[i].processor << endl;
                cout << " ����������� ������: " << p[i].RAM << " GB" << endl;
                cout << " ����������: " << p[i].video_card << endl;
                cout << " �������� : " << p[i].floppy_drive << endl;
                cout << " ���������� ������ : " << p[i].quantity << endl;
                cout << " ��� ��������: " << p[i].numb << endl;
                cout << endl;
                cout << "������������� ������� (1 - ��, 0 - ���) ? : ";
                bool final_buy;
                cin >> final_buy;
                if (final_buy) {
                    if (p[i].quantity > 0) {
                        p[i].quantity -= 1;
                        cout << "����������� � �������� �������� " << p[i].name << "\n";
                    }
                    else {
                        cout << "� ��������� ����� ���������� \n";
                    }
                }
            }
        }
    }

    return p;
    system("pause");

}

vector <Product> addProduct(vector <Product> p) {
    Product pc;

    cout << " ������� ��� ��������: ";
    int n;
    cin >> n;
    for (int i = 0; i < p.size(); i++) {
        if (n == p[i].numb) {
            cout << "����� ����� ��� ����������";
            return p;
        }
    }
    pc.numb = n;

    cout << "\n";

    cout << " ������� ��������: ";
    string name;
    cin >> name;
    pc.name = name;

    cout << "\n";

    cout << " ������� ���������: ";
    string pr;
    cin >> pr;
    pc.processor = pr;

    cout << "\n";

    cout << " ������� ����������� ������ GB : " ;
    int r;
    cin >> r;
    pc.RAM = r;

    cout << "\n";

    cout << " ������� ����������: ";
    string vc;
    cin >> vc;
    pc.video_card = vc;
        
    cout << "\n";

    cout << " ���� �������� (1 - ��, 0 - ���) : ";
    bool fd;
    cin >> fd;
    pc.floppy_drive = fd;

    cout << "\n";

    cout << " ������� ���������� ������ : ";
    int q;
    cin >> q;
    pc.quantity = q;

    p.push_back(pc);
    
    return p;
}

int main()
{
    setlocale(LC_ALL, "Russian");
    srand(time(NULL));

    vector <Product> products;

    products.push_back(addProduct(1, "PC1", 10, "Nvidia_1080", "intel_i5", 16, false));
    products.push_back(addProduct(2, "PC2", 5, "Radeon_570", "intel_i7", 16, false));
    products.push_back(addProduct(3, "PC3", 60, "Nvidia_1080", "intel_i9", 8, true));
    products.push_back(addProduct(4, "PC4", 2, "Nvidia_1080", "intel_i3", 16, false));
    products.push_back(addProduct(5, "PC5", 3, "Radeon_570", "intel_i7", 2, true));
    products.push_back(addProduct(6, "PC6", 7, "Nvidia_1080", "intel_i5", 16, false));

    while (true) {
        system("cls");
        cout << " 1 - ����� ������� �� ������ \n 2 - ����� ������� �� ��������������� \n 3 - ������ ������� \n 4 - �������� ����� \n 5 - ����� \n";
        cout << "������� ����� � �������� ������� ������ ��������� : ";
        int operation;
        cin >> operation;

        if (operation == 1) {
            findNumberProduct(products);
        }
        if (operation == 2) {
            findWordProduct(products);
        }
        if (operation == 3) {
            products = buyProduct(products);
        }
        if (operation == 4) {
            products = addProduct(products);
        }
        if (operation == 5) {
            exit;
        }
    }

}