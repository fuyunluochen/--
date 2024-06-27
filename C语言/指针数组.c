#include <stdio.h>
int main() {
  int a, b, c;
  int *arr[3] = {&a, &b, &c};
  *arr[0] = 999;
  *arr[1] = 998;
  *arr[2] = 997;
  printf("%d\n", a);
  printf("%d\n", b);
  printf("%d\n", c);
  return 0;
}