#include <stdio.h>

//@formatter:on
int main() {
//  Բ�������s=Pi*r*r;
//  Բ���ܳ���l=2*Pi*r;
  const double Pi = 3.14;
  double r, s, l;
  printf("������Բ�İ뾶��\n");
  scanf("%lf", &r);
  s = Pi * r * r;
  l = 2 * Pi * r;
  printf("Բ�������:\n");
  printf("%.2f\n", s);
  printf("Բ���ܳ��ǣ�\n");
  printf("%.2f", l);
}