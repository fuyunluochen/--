//
// Created by fuyunluochen on 2023/12/8.
//
#include <stdio.h>
void test2(int arr[]) {
  arr[1] = 999;
}
void test(int arr[]) {
  arr[0] = 999;
  test2(arr);
}
int main() {
  int arr[] = {4, 3, 8, 2, 1, 7, 5, 6, 9, 0};
  test(arr);
  printf("%d\n%d\n%d", arr[0], arr[1], arr[2]);
}

//void test() {
//  static int a = 10;
//  a += 10;
//  printf("%d\n", a);
//}
//int main() {
//
//  test();
//  test();
//  return 0;
//}

//int sum(int a, int b) {
//  return a + b;
//}
//int main() {
//  int a = 10, b = 20;
//  int result = sum(a, b);
//  printf("a+b=%d\n", sum(a, b));
//}

//int findMin(int arr[], int len);
//int main() {
//  int arr[] = {1, 4, -9, 2, -4, 7};
//  int min = findMin(arr, 6);
//  printf("第一个小于0的数是：%d\n", min);
//}
//int findMin(int arr[], int len) {
//  for (int i = 0; i < len; i++) {
//    if (arr[i] < 0) return arr[i];
//  }
//  return 0;

