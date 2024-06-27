#include <stdio.h>

//@formatter:on
int main() {
  int a, b;
  printf("请输入需要对比的2个数\n");
  scanf("%d%d", &a, &b);
  printf("最大值为:%d\n", a > b ? a : b);
  int x, y, z;
  printf("请输入需要对比的3个数\n");
  scanf("%d%d%d", &x, &y, &z);
  printf("最大值为：%d\n", x > y ? (x > z ? x : z) : (y > z ? y : z));
  return 0;
}