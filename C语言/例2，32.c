#include <stdio.h>
//@formatter:on;
int main() {
  // 实现输出100以内能被7整除的数
  for (int i = 0; i < 100; i++) {
    if (i % 7 != 0) continue;
    printf("%-3d", i);
  }
  printf("\n");
  return 0;
}
