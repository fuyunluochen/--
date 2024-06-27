#include <stdio.h>

//@formatter:on
int main() {
  int a, b, c;
  printf("请输入小猪体重:\n");
  scanf("%d%d%d", &a, &b, &c);

  if (a > c) printf("小猪a最重");
  else if (b > c) printf("小猪b最重");
  else printf("小猪c最重");
  return 0;

}