#include <iostream>

using namespace std;

#define day 7

const int month = 12;

int main() {
    cout << "一周有：" << day << "天" << endl;
//    int day=8;报错，day是常量，不支持修改
    cout << "一年有：" << month << "个月" << endl;
//    int month = 24;const标记的也是常量，同样不支持修改

    return 0;
}