#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void quickSort(int arr[], int left, int right) {  //arr是数组，left是起始下标，right是结束下标
  if (left >= right) return;
  int base = arr[left], l = left, r = right;
  while (l < r) {
    while (l < r && arr[r] >= base) r--;
    arr[l] = arr[r];
    while (l < r && arr[l] <= base) l++;
    arr[r] = arr[l];
  }
  arr[r] = base;
  quickSort(arr, left, r - 1);
  quickSort(arr, r + 1, right);
}

int main() {

  int arr[20];
  srand(time(NULL));
  for (int i = 0; i < 20; i++) {
    int num = rand() % 100 + 1;  // 生成 1 到 100 之间的随机整数
    int count = 0;
    // 判断 num 是否已存在于数组中
    for (int j = 0; j < i; j++) {
      if (arr[j] == num) {
        count++;
        break;
      }
    }
    // 如果 num 已存在于数组中，则继续生成新的随机数
    if (count > 0) {
      i--;
      continue;
    }
    arr[i] = num;  // 将 num 添加到数组中
  }
  quickSort(arr, 0, 19);  //10个数字下标就是0-9
  for (int i = 0; i < 19; ++i) {
    printf("%d ", arr[i]);
  }
}