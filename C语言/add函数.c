#include <stdio.h>

//@formatter:on
int Add(int x, int y) {
  int z;
  z = x + y;
  return z;
}

int main() {
  int a = 0, b = 0, c;
  scanf_s("%d", &a);
  scanf_s("%d", &b);
  c = Add(a, b);
  printf("%d", c);
  return 0;
}