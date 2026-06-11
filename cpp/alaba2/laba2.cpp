#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct ProductPublic {
    string name;
    string manufacturer;
    double price;
    int shelfLife;
    int quantity;

    static int count;
    static int getCount() { return count; }

    ProductPublic() : name(""), manufacturer(""), price(0.0), shelfLife(0), quantity(0) {
        ++count;
    }

    ProductPublic(const string& n, const string& m, double p, int s, int q)
        : name(n), manufacturer(m), price(p), shelfLife(s), quantity(q) {
        ++count;
    }

    ProductPublic(const ProductPublic& other)
        : name(other.name), manufacturer(other.manufacturer), price(other.price),
          shelfLife(other.shelfLife), quantity(other.quantity) {
        ++count;
    }


    ~ProductPublic() {
        --count;
    }

    double totalCost() const {
        return price * quantity;
    }

    void show() const {
        cout << name << " | " << manufacturer << " | Цена: " << price
             << " | Срок: " << shelfLife << " дн. | Кол-во: " << quantity
             << " | Стоимость: " << totalCost() << endl;
    }
};

int ProductPublic::count = 0;

class ProductPrivate {
private:
    string name;
    string manufacturer;
    double price;
    int shelfLife;
    int quantity;

    static int count;

public:
    static int getCount() { return count; }

    ProductPrivate() : name(""), manufacturer(""), price(0.0), shelfLife(0), quantity(0) {
        ++count;
    }

    ProductPrivate(const string& n, const string& m, double p, int s, int q)
        : name(n), manufacturer(m), price(p), shelfLife(s), quantity(q) {
        ++count;
    }

    ProductPrivate(const ProductPrivate& other)
        : name(other.name), manufacturer(other.manufacturer), price(other.price),
          shelfLife(other.shelfLife), quantity(other.quantity) {
        ++count;
    }

    ~ProductPrivate() {
        --count;
    }

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
        cout << name << " | " << manufacturer << " | Цена: " << price
             << " | Срок: " << shelfLife << " дн. | Кол-во: " << quantity
             << " | Стоимость: " << totalCost() << endl;
    }
};

int ProductPrivate::count = 0;

void modify_object(ProductPublic& p) {
    p.price *= 1.1;
    p.quantity += 5;
}

void try_to_modify_object(ProductPublic p) {
    p.price *= 0.9;
    p.quantity -= 3;
}

void modify_object(ProductPrivate& p) {
    p.setPrice(p.getPrice() * 1.1);
    p.setQuantity(p.getQuantity() + 5);
}

void try_to_modify_object(ProductPrivate p) {
    p.setPrice(p.getPrice() * 0.9);
    p.setQuantity(p.getQuantity() - 3);
}

vector<ProductPublic> readPublicFromFile(const string& filename) {
    vector<ProductPublic> result;
    ifstream file(filename);
    if (!file) return result;
    string line;
    while (getline(file, line)) {
        size_t p1 = line.find(',');
        size_t p2 = line.find(',', p1 + 1);
        size_t p3 = line.find(',', p2 + 1);
        size_t p4 = line.find(',', p3 + 1);
        if (p1 == string::npos || p2 == string::npos || p3 == string::npos || p4 == string::npos)
            continue;
        ProductPublic prod;
        prod.name = line.substr(0, p1);
        prod.manufacturer = line.substr(p1 + 1, p2 - p1 - 1);
        prod.price = stod(line.substr(p2 + 1, p3 - p2 - 1));
        prod.shelfLife = stoi(line.substr(p3 + 1, p4 - p3 - 1));
        prod.quantity = stoi(line.substr(p4 + 1));
        result.push_back(prod);
    }
    return result;
}

vector<ProductPrivate> readPrivateFromFile(const string& filename) {
    vector<ProductPrivate> result;
    ifstream file(filename);
    if (!file) return result;
    string line;
    while (getline(file, line)) {
        size_t p1 = line.find(',');
        size_t p2 = line.find(',', p1 + 1);
        size_t p3 = line.find(',', p2 + 1);
        size_t p4 = line.find(',', p3 + 1);
        if (p1 == string::npos || p2 == string::npos || p3 == string::npos || p4 == string::npos)
            continue;
        ProductPrivate prod;
        prod.setName(line.substr(0, p1));
        prod.setManufacturer(line.substr(p1 + 1, p2 - p1 - 1));
        prod.setPrice(stod(line.substr(p2 + 1, p3 - p2 - 1)));
        prod.setShelfLife(stoi(line.substr(p3 + 1, p4 - p3 - 1)));
        prod.setQuantity(stoi(line.substr(p4 + 1)));
        result.push_back(prod);
    }
    return result;
}

int main() {
    cout << "=== Public-класс ===" << endl;
    ProductPublic p1("Milk", "Dairy", 1.5, 10, 50);
    ProductPublic p2 = p1;
    ProductPublic p3;
    cout << "Счётчик объектов: " << ProductPublic::getCount() << endl;

    cout << "\nДо modify_object: "; p1.show();
    modify_object(p1);
    cout << "После modify_object: "; p1.show();
    try_to_modify_object(p1);
    cout << "После try_to_modify_object: "; p1.show();

    
    cout << "\nДинамическое создание (new/delete):" << endl;
    ProductPublic* dynPub = new ProductPublic("Bread", "Bakery", 0.8, 5, 100);
    cout << "Счётчик после new: " << ProductPublic::getCount() << endl;
    delete dynPub;
    cout << "Счётчик после delete: " << ProductPublic::getCount() << endl;

    cout << "\n=== Private-класс ===" << endl;
    ProductPrivate pr1("Butter", "Dairy", 1.8, 15, 40);
    ProductPrivate pr2 = pr1;
    cout << "Счётчик объектов: " << ProductPrivate::getCount() << endl;

    cout << "\nДо modify_object: "; pr1.show();
    modify_object(pr1);
    cout << "После modify_object: "; pr1.show();

    ProductPrivate* dynPriv = new ProductPrivate("Cheese", "Dairy", 2.2, 20, 30);
    cout << "Счётчик после new: " << ProductPrivate::getCount() << endl;
    delete dynPriv;
    cout << "Счётчик после delete: " << ProductPrivate::getCount() << endl;

    string filename = "products.txt";
    string targetName;
    double maxPrice;
    int minShelfLife;

    cout << "\nВведите наименование товара: ";
    getline(cin, targetName);
    cout << "Введите максимальную цену: ";
    cin >> maxPrice;
    cout << "Введите минимальный срок хранения: ";
    cin >> minShelfLife;

    auto pubVec = readPublicFromFile(filename);
    cout << "\n--- Public-версия ---" << endl;
    cout << "а) Список товаров '" << targetName << "':" << endl;
    for (const auto& p : pubVec)
        if (p.name == targetName) p.show();

    cout << "\nб) Товары '" << targetName << "' с ценой <= " << maxPrice << ":" << endl;
    for (const auto& p : pubVec)
        if (p.name == targetName && p.price <= maxPrice) p.show();

    cout << "\nв) Товары со сроком хранения > " << minShelfLife << ":" << endl;
    for (const auto& p : pubVec)
        if (p.shelfLife > minShelfLife) p.show();

    auto privVec = readPrivateFromFile(filename);
    cout << "\n--- Private-версия ---" << endl;
    cout << "а) Список товаров '" << targetName << "':" << endl;
    for (const auto& p : privVec)
        if (p.getName() == targetName) p.show();

    cout << "\nб) Товары '" << targetName << "' с ценой <= " << maxPrice << ":" << endl;
    for (const auto& p : privVec)
        if (p.getName() == targetName && p.getPrice() <= maxPrice) p.show();

    cout << "\nв) Товары со сроком хранения > " << minShelfLife << ":" << endl;
    for (const auto& p : privVec)
        if (p.getShelfLife() > minShelfLife) p.show();

    cout << "\nИтоговые счётчики (должны быть 0):" << endl;
    cout << "ProductPublic: " << ProductPublic::getCount() << endl;
    cout << "ProductPrivate: " << ProductPrivate::getCount() << endl;

    return 0;
}