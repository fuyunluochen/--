#include <stdio.h>

//@formatter:on
int main(void) {
//    无符号 unsigned 有符号 signed(可以省略)
  unsigned int a = -10;
  int b = 10;
  int c = 0567;
  printf("%o", c);
  printf("%X\n", b);
  printf("%d", a);
  return 0;
}