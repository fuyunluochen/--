#include <stdio.h>
//@formatter:on
int main() {
  int i, j;
  int k = 0;
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      k++;
    }
  }
  printf("%d", k);
  return 0;
}
