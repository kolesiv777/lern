#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Goods {
protected:
    string name;
    string manufacturer;
    double price;

public:
    Goods() : name(""), manufacturer(""), price(0.0) {}
    Goods(const string& n, const string& m, double p) : name(n), manufacturer(m), price(p) {}
    Goods(const Goods& other) : name(other.name), manufacturer(other.manufacturer), price(other.price) {}
    virtual ~Goods() {}

    void setName(const string& n) { name = n; }
    void setManufacturer(const string& m) { manufacturer = m; }
    void setPrice(double p) { price = p; }
    string getName() const { return name; }
    string getManufacturer() const { return manufacturer; }
    double getPrice() const { return price; }

    virtual void show() const {
        cout << "Goods: " << name << " | Manufacturer: " << manufacturer
             << " | Price: " << price;
    }
};

class Product : public Goods {
private:
    int shelfLife;
    int quantity;

public:
    Product() : Goods(), shelfLife(0), quantity(0) {}
    Product(const string& n, const string& m, double p, int s, int q)
        : Goods(n, m, p), shelfLife(s), quantity(q) {}
    Product(const Product& other) : Goods(other), shelfLife(other.shelfLife), quantity(other.quantity) {}
    ~Product() {}

    void setShelfLife(int s) { shelfLife = s; }
    void setQuantity(int q) { quantity = q; }
    int getShelfLife() const { return shelfLife; }
    int getQuantity() const { return quantity; }

    double totalCost() const { return price * quantity; }

   void show() const override {
        Goods::show();
        cout << " | Shelf life: " << shelfLife << " days | Quantity: " << quantity
             << " | Total cost: " << totalCost() << endl;
    }
};

class Plant : public Goods {
private:
    string plantType;
    int ageMonths;

public:
    Plant() : Goods(), plantType(""), ageMonths(0) {}
    Plant(const string& n, const string& m, double p, const string& type, int age)
        : Goods(n, m, p), plantType(type), ageMonths(age) {}
    Plant(const Plant& other) : Goods(other), plantType(other.plantType), ageMonths(other.ageMonths) {}
    ~Plant() {}

    void setPlantType(const string& t) { plantType = t; }
    void setAgeMonths(int a) { ageMonths = a; }
    string getPlantType() const { return plantType; }
    int getAgeMonths() const { return ageMonths; }

    string waterDemand() const {
        if (ageMonths < 6) return "Frequent watering";
        else if (ageMonths < 24) return "Moderate watering";
        else return "Rare watering";
    }

    void show() const override {
        Goods::show();
        cout << " | Type: " << plantType << " | Age: " << ageMonths
             << " months | Watering: " << waterDemand() << endl;
    }
};

int main() {
    const int SIZE = 6;
    Goods* items[SIZE];

    items[0] = new Product("Milk", "Dairy", 1.5, 10, 50);
    items[1] = new Product("Bread", "Bakery", 0.8, 5, 100);
    items[2] = new Product("Cheese", "Dairy", 2.2, 20, 30);

    items[3] = new Plant("Ficus", "Holland", 750.0, "Ficus Benjamina", 18);
    items[4] = new Plant("Cactus", "Mexico", 250.0, "Echinopsis", 36);
    items[5] = new Plant("Orchid", "Thailand", 1200.0, "Phalaenopsis", 8);

    cout << "=== Polymorphic output ===" << endl;
    for (int i = 0; i < SIZE; ++i) {
        items[i]->show();
    }

    for (int i = 0; i < SIZE; ++i) {
        delete items[i];
    }

    return 0;
}