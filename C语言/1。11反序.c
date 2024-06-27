#include <stdio.h>
//@formatter:on
int ReverseOrder(int x) {
  printf("%d\n倒序后:\n", x);
  while (x > 0) {
    printf("%d", x % 10);
    x /= 10;
  }
  printf("\n");
  return 0;
}
int ReverseOrder2(int x) {
  printf("%d\n倒序后:\n", x);
  do {
    printf("%d", x % 10);
    x /= 10;
  } while (x > 0);
  return 0;
}
int main() {
  int x;
  int y;
  printf("请输入一串整数：\n");
  scanf_s("%d", &x);
  printf("请选择调用函数：");
  scanf_s("%d", &y);
  if (y == 1) {
    ReverseOrder(x);
  } else if (y == 2) {
    ReverseOrder2(x);
  }
  return 0;
}