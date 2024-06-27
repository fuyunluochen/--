#include <stdio.h>
int main() {
  int a = 20;  // 定义一个整型变量a并初始化为20
  int *p = &a;  // 定义一个整型指针变量p，并将它的值指向变量a的地址
  int **pp = &p;  // 定义一个整型指针变量pp，并将它的值指向变量p的地址
  int ***ppp = &pp;  // 定义一个整型指针变量ppp，并将它的值指向变量pp的地址
  printf("%p=%d\n", ppp, ***ppp);  // 打印指针变量ppp所指向的指针变量所指向的指针变量所指向的变量的地址和值
  printf("p = %p, a = %d\n", p, *p);  // 打印p的值以及p指向的值
  printf("p = %p, a = %d\n", pp, **pp);  // 打印pp的值以及pp指向的值所指向的值
  printf("p = %p, a = %d\n", ppp, ***ppp);  // 打印ppp的值以及ppp指向的值所指向的值所指向的值


  return 0;  // 返回0

}