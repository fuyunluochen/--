#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 20
//@formatter:on
int main() {
  int t, swap_flag;
  int random_num[N];
  srand(time(NULL));
  for (int i = 0; i < N; i++)
    random_num[i] = rand() % 100 + 1;
  printf("排序前：");
  for (int i = 0; i < N; i++)
    printf("%5d", random_num[i]);
  printf("\n");
//  冒泡排序法（有小到大）：小数在前面，大数在后面
  for (int i = 0; i < N; i++) {
    swap_flag = 0;
    for (int j = 0; j < N - i; j++) {
      if (random_num[j] > random_num[j + 1]) {
        t = random_num[j];
        random_num[j] = random_num[j + 1];
        random_num[j + 1] = t;
        swap_flag = 1;
      }
    }
    if (swap_flag == 0) break;
  }
  printf("排序后：");
  for (int i = 0; i < N; i++) {
    printf("%5d", random_num[i]);
  }
  printf("\n");
  return 0;
}
