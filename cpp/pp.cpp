#include <iostream>
#include <string>

int main() {
    
    int age;
    double height;
    std::string name;
    int numbers[5] = {10, 20, 30, 40, 50};
    
    std::cout << "===== ПРОВЕРКА РАБОТЫ C++ =====\n";
    std::cout << "Введите ваше имя: ";
    
    // Ввод строки
    std::getline(std::cin, name);
    
    std::cout << "Введите ваш возраст: ";
    std::cin >> age;
    
    std::cout << "Введите ваш рост (в метрах, например 1.75): ";
    std::cin >> height;
    
    // Вывод введенных данных
    std::cout << "\n--- ВЫ ВВЕЛИ ---\n";
    std::cout << "Имя: " << name << std::endl;
    std::cout << "Возраст: " << age << " лет" << std::endl;
    std::cout << "Рост: " << height << " м" << std::endl;
    
    // Условный оператор
    std::cout << "\n--- ПРОВЕРКА УСЛОВИЙ ---\n";
    if (age >= 18) {
        std::cout << name << ", вы совершеннолетний\n";
    } else {
        std::cout << name << ", вы несовершеннолетний\n";
    }
    
    if (height > 1.80) {
        std::cout << "У вас высокий рост\n";
    } else if (height > 1.60) {
        std::cout << "У вас средний рост\n";
    } else {
        std::cout << "У вас небольшой рост\n";
    }
    
    // Цикл for
    std::cout << "\n--- ЦИКЛ FOR (массив чисел) ---\n";
    std::cout << "Числа в массиве: ";
    for (int i = 0; i < 5; i++) {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;
    
    // Цикл while с подсчетом
    std::cout << "\n--- ЦИКЛ WHILE (счет от 1 до 5) ---\n";
    int counter = 1;
    while (counter <= 5) {
        std::cout << "Счет: " << counter << std::endl;
        counter++;
    }
    
    // Простая арифметика
    std::cout << "\n--- АРИФМЕТИКА ---\n";
    int a = 15, b = 4;
    std::cout << a << " + " << b << " = " << (a + b) << std::endl;
    std::cout << a << " - " << b << " = " << (a - b) << std::endl;
    std::cout << a << " * " << b << " = " << (a * b) << std::endl;
    std::cout << a << " / " << b << " = " << (a / b) << " (целочисленное деление)" << std::endl;
    std::cout << a << " % " << b << " = " << (a % b) << " (остаток)" << std::endl;
    std::cout << a << " / " << b << " = " << (static_cast<double>(a) / b) << " (вещественное деление)" << std::endl;
    
    std::cout << "\n===== ПРОГРАММА ЗАВЕРШЕНА УСПЕШНО =====\n";
    
    return 0;
}