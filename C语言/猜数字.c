#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
  srand((unsigned) time(NULL));
  int a = rand() % 30;
  while (1) {
    int i;
    printf("请输入任意一个数:\n");
    scanf_s("%d", &i);
    if (i > a) {
      printf("猜大了\n");
    } else {
      printf("猜小了\n");
    }
    if (i == a) {
      printf("猜对了！");
      break;
    }
  }
  return 0;
}