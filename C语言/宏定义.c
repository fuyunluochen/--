#include <stdio.h>
//@formatter:on
void macro_Definition() {
#define pi 3.1415926
  float s, l, r = 0;
  //  圆的面积：s=Pi*r*r;
  //  圆的周长：l=2*Pi*r;
  printf("请输入圆的半径：\n");
  scanf("%f", &r);
  s = pi * r * r;
  l = 2 * pi * r;

  printf("圆的半径为：%.2f\n", r);
  printf("圆的面积为：%.2f\n", s);
  printf("圆的周长为：%.2f\n", l);
//  终止宏定义作用域
#undef pi
}
void Parameterized_Macro_Definition() {
#define Pi 3.1415926
#define S(r) Pi *(r) * (r)
  float a, s;
  printf("请输入一个非负数：\n");
  scanf("%f", &a);
  s = S(a);
  printf("圆的半径是：%.2f\n", a);
  printf("圆的面积是：%.2f\n", s);
}
void Max() {
#define MAX(x, y) (x > y ? x : y)
  int x, y;
  printf("请输入任意两个整数：\n");
  scanf("%d%d", &x, &y);
  printf("最大数是：%d\n", MAX(x, y));
}
int main() {
  macro_Definition();
  Parameterized_Macro_Definition();
  Max();
  return 0;
}