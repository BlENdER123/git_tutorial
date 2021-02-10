// Задорожний Антон 219/5
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

    cout << "Введите код товара : ";
    int n;
    cin >> n;

    for (int i = 0; i < p.size(); i++) {
        if (p[i].numb == n) {
            cout << " Название: " << p[i].name << endl;
            cout << " Процессор: " << p[i].processor << endl;
            cout << " Оперативная память: " << p[i].RAM << " GB" << endl;
            cout << " Видеокарта: " << p[i].video_card << endl;
            cout << " Дисковод : " << p[i].floppy_drive << endl;
            cout << " Количество товара : " << p[i].quantity << endl;
            cout << " Код продукта: " << p[i].numb << endl;
        }
    }
    system("pause");
}

void findWordProduct(vector <Product> p)
{
    string vc;
    cout << "Введите нужную видеокарту : ";
    cin >> vc;

    cout << "\n";

    string pr;
    cout << "Введите нужный процессор : ";
    cin >> pr;

    cout << "\n";

    int r;
    cout << "Введите нужное количество оперативной памяти : ";
    cin >> r;

    cout << "\n";

    bool fd;
    cout << "Нужен дисковод (1 - да, 0 - нет) :  ";
    cin >> fd;

    cout << "\n";

    for (int i = 0; i < p.size(); i++) {
        if ((vc == p[i].video_card) & (pr == p[i].processor) & (r == p[i].RAM) & (fd == p[i].floppy_drive)) {
            cout << " Название: " << p[i].name << endl;
            cout << " Процессор: " << p[i].processor << endl;
            cout << " Оперативная память: " << p[i].RAM << " GB" << endl;
            cout << " Видеокарта: " << p[i].video_card << endl;
            cout << " Дисковод : " << p[i].floppy_drive << endl;
            cout << " Количество товара : " << p[i].quantity << endl;
            cout << " Код продукта: " << p[i].numb << endl;
            cout << endl;
        }
    }
    system("pause");
}

vector <Product> buyProduct(vector <Product> p) {

    cout << "Желаете купить ПК (1 - да, 0 - нет) ? :  ";
    bool buy;
    cin >> buy;

    if (buy) {
        cout << "Введите код товара : ";
        int n;
        cin >> n;

        for (int i = 0; i < p.size(); i++) {
            if (n == p[i].numb) {
                cout << " Название: " << p[i].name << endl;
                cout << " Процессор: " << p[i].processor << endl;
                cout << " Оперативная память: " << p[i].RAM << " GB" << endl;
                cout << " Видеокарта: " << p[i].video_card << endl;
                cout << " Дисковод : " << p[i].floppy_drive << endl;
                cout << " Количество товара : " << p[i].quantity << endl;
                cout << " Код продукта: " << p[i].numb << endl;
                cout << endl;
                cout << "Подтверждаете покупку (1 - да, 0 - нет) ? : ";
                bool final_buy;
                cin >> final_buy;
                if (final_buy) {
                    if (p[i].quantity > 0) {
                        p[i].quantity -= 1;
                        cout << "Поздравляем с успешной покупкой " << p[i].name << "\n";
                    }
                    else {
                        cout << "К сожалению товар закончился \n";
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

    cout << " Введите код продукта: ";
    int n;
    cin >> n;
    for (int i = 0; i < p.size(); i++) {
        if (n == p[i].numb) {
            cout << "Такой товар уже существует";
            return p;
        }
    }
    pc.numb = n;

    cout << "\n";

    cout << " Введите название: ";
    string name;
    cin >> name;
    pc.name = name;

    cout << "\n";

    cout << " Введите процессор: ";
    string pr;
    cin >> pr;
    pc.processor = pr;

    cout << "\n";

    cout << " Введите оперативную память GB : " ;
    int r;
    cin >> r;
    pc.RAM = r;

    cout << "\n";

    cout << " Введите видеокарту: ";
    string vc;
    cin >> vc;
    pc.video_card = vc;
        
    cout << "\n";

    cout << " Есть дисковод (1 - да, 0 - нет) : ";
    bool fd;
    cin >> fd;
    pc.floppy_drive = fd;

    cout << "\n";

    cout << " Введите количество товара : ";
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
        cout << " 1 - найти продукт по номеру \n 2 - найти продукт по характеристикам \n 3 - купить продукт \n 4 - добавить товар \n 5 - выйти \n";
        cout << "Введите цифру с функцией которую хотите выполнить : ";
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