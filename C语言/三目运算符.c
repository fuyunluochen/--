#include <stdio.h>

//@formatter:on
int main() {
  int a, b;
  printf("��������Ҫ�Աȵ�2����\n");
  scanf("%d%d", &a, &b);
  printf("���ֵΪ:%d\n", a > b ? a : b);
  int x, y, z;
  printf("��������Ҫ�Աȵ�3����\n");
  scanf("%d%d%d", &x, &y, &z);
  printf("���ֵΪ��%d\n", x > y ? (x > z ? x : z) : (y > z ? y : z));
  return 0;
}