#include <stdio.h>

int main() {
  char str[] = "hello world!";  // 定义一个字符串，内容为"hello world!"
  char *p = str;  // 定义一个指针变量p，并将指针指向字符串str的首地址
  printf("%c\n", *p);  // 输出指针p指向的字符
  printf("%c\n", p[1]);  // 输出字符串p的第二个字符

  for (int i = 0; i < 12; i++) {  // 循环12次，从0到11
    printf("%c", *(p + i));  // 输出指针p加上i所指向的字符
  }
  printf("\n");  // 输出换行符

  printf("%c\n", *(p + 2));  // 打印位于指针p之后第3个元素的值
  printf("%c\n", *p + 1);    // 打印指针p指向的元素的下一个元素的值
  p++;  // p自增1
  printf("%c\n", *(p + 1));  // 打印位于指针p之后第二个元素所指向的字符及其对应的新行符

  return 0;
}
