#include <iostream>
#include <time.h>
#include <stdio.h>

using namespace std;

float pi = 3.1415926;

double pi2 = 3.1415926;

int main() {
    double dur;
    clock_t start, end;
    start = clock();
    dur = (double) (end - start);
    printf("Use Time:%f\n", (dur / CLOCKS_PER_SEC));
    //  默认情况下，输出一个浮点数，只会显示6位小数
    cout << "pi=" << pi << endl;
    cout << "pi2=" << pi2 << endl;
    cout << "float占用内存为:" << sizeof(float) << endl;
    cout << "double占用内存为:" << sizeof(double) << endl;
    end = clock();
    system("pause");
    return 0;
}