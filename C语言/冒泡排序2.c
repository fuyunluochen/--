#include <stdio.h>
#define N 10
int main() {
  int t, swap;
  int arr[N];
  printf("������%d������\n", N);
  for (int i = 0; i < N; i++) {
    scanf_s("%d", &arr[i]);
  }
  printf("����ǰ:\n");
  for (int i = 0; i < N; i++) {
    printf("%5d", arr[i]);
  }
  printf("\n");
  for (int i = 0; i < N; i++) {
    swap = 0;
    for (int j = 0; j < N - i; j++) {
      if (arr[j] > arr[j + 1]) {
        t = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = t;
        swap = 1;
      }
    }
    if (swap == 0) break;
  }
  printf("�����:\n");
  for (int i = 0; i < N; i++) {
    printf("%5d", arr[i]);
  }
  printf("\n");
  return 0;
}