#include <iostream>

using namespace std;

int a = 20;

int main() {
    out << "short占用内存为：" << sizeof(short) << endl;
    cout << "int占用内存为：" << sizeof(int) << endl;
    cout << "long占用内存为：" << sizeof(long) << endl;
    cout << "long long占用内存为：" << sizeof(long long) << endl;
    return 0;
}
