#include <stdio.h>
//@formatter:on
int main() {
  int x;
  double sum = 0;
  int cnt = 0;
  printf("输入任意整数（输入-1结束输入）:\n");
  scanf_s("%d", &x);
  //  输入-1结束输入
  while (x != -1) {
    sum += x;
    cnt++;
    scanf_s("%d", &x);
  }
  if (cnt > 0) {
    printf("%.1f\n", sum / cnt);
  }
}