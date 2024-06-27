#include <stdio.h>
//@formatter:on
int main(void) {
  char ch;
  printf("请输入一串字符串(以#结尾):\n");
  while ((ch = getchar()) != '#')
    putchar(ch);
  putchar('\n');
  return 0;
}