#include <stdio.h>
#include <string.h>
int main() {
  char c[2];
  printf("可以输入了");
  scanf_s("%s", &c);
  printf("%s", c);
}