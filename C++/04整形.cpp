#include <iostream>

using namespace std;

int main() {
//    短整形(-32768-32767)
    short num1 = 32767;
//    整形(-2147483648-2147483647)
    int num2 = 2147483647;
//    长整形(-2147483648-2147483647)
    long num3 = 2147483647;
//    长长整形(-9223372036854775808-9223372036854775807)
    long long num4 = 9223372036854775807;
    std::cout << num1 << endl;
    std::cout << num2 << endl;
    std::cout << num3 << endl;
    std::cout << num4 << endl;
}
