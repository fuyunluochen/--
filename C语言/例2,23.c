#include <stdio.h>
//@formatter:on
int main(void) {
  char ch;
  printf("������һ���ַ���(��#��β):\n");
  while ((ch = getchar()) != '#')
    putchar(ch);
  putchar('\n');
  return 0;
}