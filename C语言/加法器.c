#include <stdio.h>
int add(int x, int y) {
  int z;
  z = x + y;
  printf("%d+%d=%d\n", x, y, z);
}
int main() {
  int x = 0, y = 0;
  for (int i = 0; i < 10; i++) {
    scanf("%d%d", &x, &y);
    add(x, y);
  }

  return 0;
}