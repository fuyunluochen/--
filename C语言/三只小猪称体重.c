#include <stdio.h>

//@formatter:on
int main() {
  int a, b, c;
  printf("������С������:\n");
  scanf("%d%d%d", &a, &b, &c);

  if (a > c) printf("С��a����");
  else if (b > c) printf("С��b����");
  else printf("С��c����");
  return 0;

}