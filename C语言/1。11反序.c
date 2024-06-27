#include <stdio.h>
//@formatter:on
int ReverseOrder(int x) {
  printf("%d\n�����:\n", x);
  while (x > 0) {
    printf("%d", x % 10);
    x /= 10;
  }
  printf("\n");
  return 0;
}
int ReverseOrder2(int x) {
  printf("%d\n�����:\n", x);
  do {
    printf("%d", x % 10);
    x /= 10;
  } while (x > 0);
  return 0;
}
int main() {
  int x;
  int y;
  printf("������һ��������\n");
  scanf_s("%d", &x);
  printf("��ѡ����ú�����");
  scanf_s("%d", &y);
  if (y == 1) {
    ReverseOrder(x);
  } else if (y == 2) {
    ReverseOrder2(x);
  }
  return 0;
}