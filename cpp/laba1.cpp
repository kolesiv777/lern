#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

// struct все открытые по умолчанию 
struct ProductPublic {
    string name, manufacturer;
    double price;
    int shelfLife, quantity;

    double totalCost() const { return price * quantity; }

    void show() const {
        cout << name << " | " << manufacturer << " | " << price
             << " | " << shelfLife << " дн | " << quantity
             << " | Сумма: " << totalCost() << endl;
    }
};

// class все звкрытые по умолчанию 
class ProductPrivate {
    string name, manufacturer;
    double price;
    int shelfLife, quantity;
public:
    void setName(const string& n) { name = n; }
    void setManufacturer(const string& m) { manufacturer = m; }
    void setPrice(double p) { price = p; }
    void setShelfLife(int s) { shelfLife = s; }
    void setQuantity(int q) { quantity = q; }

    string getName() const { return name; }
    string getManufacturer() const { return manufacturer; }
    double getPrice() const { return price; }
    int getShelfLife() const { return shelfLife; }
    int getQuantity() const { return quantity; }

    double totalCost() const { return price * quantity; }

    void show() const {
        cout << name << " | " << manufacturer << " | " << price
             << " | " << shelfLife << " дн | " << quantity
             << " | Сумма: " << totalCost() << endl;
    }
};

// Чтение данных из файла (формат: Название,Производитель,Цена,Срок,Количество)
vector<ProductPublic> readPublic(const string& file) {
    vector<ProductPublic> v;
    ifstream f(file);
    string line;
    while (getline(f, line)) {
        size_t p1 = line.find(','), p2 = line.find(',', p1+1),
               p3 = line.find(',', p2+1), p4 = line.find(',', p3+1);
        ProductPublic prod;
        prod.name = line.substr(0, p1);
        prod.manufacturer = line.substr(p1+1, p2-p1-1);
        prod.price = stod(line.substr(p2+1, p3-p2-1));
        prod.shelfLife = stoi(line.substr(p3+1, p4-p3-1));
        prod.quantity = stoi(line.substr(p4+1));
        v.push_back(prod);
    }
    return v;
}

vector<ProductPrivate> readPrivate(const string& file) {
    vector<ProductPrivate> v;
    ifstream f(file);
    string line;
    while (getline(f, line)) {
        size_t p1 = line.find(','), p2 = line.find(',', p1+1),
               p3 = line.find(',', p2+1), p4 = line.find(',', p3+1);
        ProductPrivate prod;
        prod.setName(line.substr(0, p1));
        prod.setManufacturer(line.substr(p1+1, p2-p1-1));
        prod.setPrice(stod(line.substr(p2+1, p3-p2-1)));
        prod.setShelfLife(stoi(line.substr(p3+1, p4-p3-1)));
        prod.setQuantity(stoi(line.substr(p4+1)));
        v.push_back(prod);
    }
    return v;
}

int main() {
    string filename = "products.txt";

    string targetName;
    double maxPrice;
    int minShelfLife;

    cout << "Введите наименование товара: ";
    getline(cin, targetName);

    cout << "Введите максимальную цену: ";
    cin >> maxPrice;

    cout << "Введите минимальный срок хранения (дней): ";
    cin >> minShelfLife;



    //Работа с public версией
    auto pub = readPublic(filename);
    cout << "\n=== ProductPublic ===\n";

    cout << "а) Список товаров '" << targetName << "':\n";
    for (const auto& p : pub)
        if (p.name == targetName) p.show();

    cout << "\nб) Товары '" << targetName << "' с ценой <= " << maxPrice << ":\n";
    for (const auto& p : pub)
        if (p.name == targetName && p.price <= maxPrice) p.show();

    cout << "\nв) Товары со сроком хранения > " << minShelfLife << ":\n";
    for (const auto& p : pub)
        if (p.shelfLife > minShelfLife) p.show();

    //Работа с private версией
    auto priv = readPrivate(filename);
    cout << "\n=== ProductPrivate ===\n";

    cout << "а) Список товаров '" << targetName << "':\n";
    for (const auto& p : priv)
        if (p.getName() == targetName) p.show();

    cout << "\nб) Товары '" << targetName << "' с ценой <= " << maxPrice << ":\n";
    for (const auto& p : priv)
        if (p.getName() == targetName && p.getPrice() <= maxPrice) p.show();

    cout << "\nв) Товары со сроком хранения > " << minShelfLife << ":\n";
    for (const auto& p : priv)
        if (p.getShelfLife() > minShelfLife) p.show();

    return 0;
}