#include <iostream>

using namespace std;
//字符型变量定义
char ch = 'A';

//字符型常见错误
//char ch2 = "c"; 定义字符型变量需要使用单引号‘’;
//char ch3 = 'abcdefg';字符型变量单引号内只能有1个


int main() {
    cout << ch << endl;
//    字符型变量占用内存
    cout << sizeof(ch) << "字节" << endl;
//字符型变量对应ASCII编码
    cout << int(ch) << endl;
    system("pause");
    return 0;
}