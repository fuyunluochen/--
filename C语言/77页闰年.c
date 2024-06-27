#include <stdio.h>
//@formatter:on
int main() {
  int year;
  while (1) {
    printf("请输入任意年份：(输入0000退出)\n");
    scanf_s("%d", &year);
    if (year == 0000) {
      printf("已退出");
      break;
    }
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
      printf("%d是闰年\n", year);
    } else {
      printf("%d不是闰年\n", year);
    }
  }
  return 0;
}