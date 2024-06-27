#include <stdio.h>
int main() {
  int arr[][3] = {{1, 2, 3}, {4, 5, 6}};
  int *p = arr[0];
  printf("%d=%d", *(p + 1), arr[0][1]);
  return 0;
}
