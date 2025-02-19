#include <stdio.h>
int main() {
  int arr[3] = {1, 2, 3}; // 定义一个包含3个元素的整型数组arr，并初始化
  int (*p)[3] = &arr; // 定义一个指向3元数组的指针p，并将arr的地址赋值给p
  for (int i = 0; i < 3; i++) { // 循环遍历ar数组中的每一行
    printf("%d\n", *(*p + i)); // 输出ar数组中第i行的内容
  }
  int ar[][3] = {{111, 222, 333}, {444, 555, 666}}; // 定义一个3元数组ar，初始化为{{111, 222, 333}, {444, 555, 666}}
  (*p)[3] = &ar; // 将ar数组的地址赋值给p的第3个元素
  printf("%d", *(*p + 1)); // 输出p的第2个元素的第一个元素
  return 0; // 返回0，表示程序执行成功结束
}