#include <stdio.h>
//@foramatter:on
int main() {
  for (int i = 1; i <= 5; ++i) {
    if (i == 3) break;
    printf("%d", i);
  }
  printf("\n");
  for (int j = 1; j <= 5; j++) {
    if (j == 3) continue;
    printf("%d", j);
  }
  return 0;
}