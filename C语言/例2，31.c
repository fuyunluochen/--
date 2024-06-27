#include <stdio.h>
//@formatter:on
int main() {
  int i, sum = 0;
  for (i = 1;; i++) {
    sum += i * i;
    if (sum > 1000) break;
  }
  printf("sum=%d,i=%d", sum, i);
  return 0;
}