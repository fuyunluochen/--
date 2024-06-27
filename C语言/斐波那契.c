#include <stdio.h>
#include<time.h>
//int main() {
//  clock_t start = clock();
//  int target = 2000;
//  int dp[target];
//  dp[1] = dp[0] = 1;
//  for (int i = 2; i < target; i++) {
//    dp[i] = dp[i - 1] + dp[i - 2];
//  }
//  printf("%d\n", dp[target - 1]);
//  clock_t end = clock();
//  double time_taken = ((double) (end - start)) / CLOCKS_PER_SEC;
//  printf("程序执行时间:%f 秒\n", time_taken);
//  return 0;
//}

//斐波那契数列
int fib(int n) {
  if (n == 1 || n == 2) return 1;
  return fib(n - 1) + fib(n - 2);
}
int main() {
  printf("%d\n", fib(6));
}
