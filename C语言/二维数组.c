#include <stdio.h>
int main() {
  int a[3][4];
  printf("请输入任意12个整数:\n");
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
      scanf_s("%d", &a[i][j]);
    }
  }
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
      printf("a[%d][%d]=%d\n", i, j, a[i][j]);
    }
  }
  return 0;
}