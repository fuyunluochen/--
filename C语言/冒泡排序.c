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
  printf("����ǰ��");
  for (int i = 0; i < N; i++)
    printf("%5d", random_num[i]);
  printf("\n");
//  ð�����򷨣���С���󣩣�С����ǰ�棬�����ں���
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
  printf("�����");
  for (int i = 0; i < N; i++) {
    printf("%5d", random_num[i]);
  }
  printf("\n");
  return 0;
}
