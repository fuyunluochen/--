#include <stdio.h>

//@formatter:on
int main() {
//  圆的面积：s=Pi*r*r;
//  圆的周长：l=2*Pi*r;
  const double Pi = 3.14;
  double r, s, l;
  printf("请输入圆的半径：\n");
  scanf("%lf", &r);
  s = Pi * r * r;
  l = 2 * Pi * r;
  printf("圆的面积是:\n");
  printf("%.2f\n", s);
  printf("圆的周长是：\n");
  printf("%.2f", l);
}