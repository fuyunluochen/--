//
// Created by fuyunluochen on 2023/12/8.
//
#include <stdio.h>

//void test() {
//  printf("hello world\n");
//  test();
//}
//int main() {
//  test();
//  return 0;
//}

//阶乘
int test(int n) {
  if (n == 1) return 1;
  return test(n - 1) * n;
}
int main() {
  int number;
  printf("请输入一个数：");
  scanf("%d", &number);
  printf("%d\n", test(number));
}