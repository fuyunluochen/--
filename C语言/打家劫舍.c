#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int Resident(int x) {
  int arr[x], size = x, result;
  for (int i = 0; i < x; i++) {
    arr[i] = rand() % 1000;
  }
  for (int i = 0; i < x; i++) {
    printf("%6d", arr[i]);
  }
  printf("\n");
  int dp[size];
  dp[0] = arr[0];
  dp[1] = arr[1] > arr[0] ? arr[1] : arr[0];
  for (int i = 2; i < size; i++) {
    dp[i] = dp[i - 1] > dp[i - 2] + arr[i] ? dp[i - 1] : dp[i - 2] + arr[i];
  }
  result = dp[size - 1];
  printf("能偷到%d元\n", result);
}
int main() {
  clock_t start = clock();
  srand(time(NULL));
  int num = rand() % 100 + 1;
  printf("街道上共有住户%d户\n", num);
  Resident(num);
  clock_t end = clock();
  double time_taken = ((double) (end - start)) / CLOCKS_PER_SEC;
  printf("程序执行时间：%f 秒\n", time_taken);
  return 0;
}
//#include <stdio.h>
//#include <stdlib.h>
//#include <time.h>
//
//void Resident(int x) {
//  int result = 0, prev = 0, curr = 0;
//  for (int i = 0; i < x; i++) {
//    int amount = rand() % 1000;
//    curr = amount > prev ? amount : prev + amount;
//    result = curr > result ? curr : result;
//    prev = curr;
//  }
//  printf("能偷到%d元\n", result);
//}
//
//int main() {
//  srand(time(NULL));
//  int num = rand() % 100 + 1;
//  printf("街道上共有住户%d户\n", num);
//  Resident(num);
//  clock_t end = clock();
//  double time_taken = ((double) (end - clock())) / CLOCKS_PER_SEC;
//  printf("程序执行时间：%f 秒\n", time_taken);
//  return 0;
//}
