#include <stdio.h>
//@formatter:on
void macro_Definition() {
#define pi 3.1415926
  float s, l, r = 0;
  //  Բ�������s=Pi*r*r;
  //  Բ���ܳ���l=2*Pi*r;
  printf("������Բ�İ뾶��\n");
  scanf("%f", &r);
  s = pi * r * r;
  l = 2 * pi * r;

  printf("Բ�İ뾶Ϊ��%.2f\n", r);
  printf("Բ�����Ϊ��%.2f\n", s);
  printf("Բ���ܳ�Ϊ��%.2f\n", l);
//  ��ֹ�궨��������
#undef pi
}
void Parameterized_Macro_Definition() {
#define Pi 3.1415926
#define S(r) Pi *(r) * (r)
  float a, s;
  printf("������һ���Ǹ�����\n");
  scanf("%f", &a);
  s = S(a);
  printf("Բ�İ뾶�ǣ�%.2f\n", a);
  printf("Բ������ǣ�%.2f\n", s);
}
void Max() {
#define MAX(x, y) (x > y ? x : y)
  int x, y;
  printf("��������������������\n");
  scanf("%d%d", &x, &y);
  printf("������ǣ�%d\n", MAX(x, y));
}
int main() {
  macro_Definition();
  Parameterized_Macro_Definition();
  Max();
  return 0;
}