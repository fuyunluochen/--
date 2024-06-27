#include <stdio.h>
//@formatter:on
void linear_array() {
  int a[100];
  for (int i = 0; i <= 99; i++) a[i] = i;
  for (int j = 100; j >= 0; j--) printf("%d\n", a[j]);
  printf("\n");
}
void two_dimensional_array() {
  int a[3][4];
  printf("请输入12个整数：\n");
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
      scanf("%d", &a[i][j]);
    }
  }
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
      printf("a[%d][%d]=%d\n", i, j, a[i][j]);
    }
  }
}
int main() {
  //   linear_array();
  two_dimensional_array();
  return 0;
}