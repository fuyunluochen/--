#include <stdio.h>
//@formatter:on
void Whileloop(int x) {
  int i = 0, sum = 0;
  while (i <= x) {
    sum = sum + i;
    printf("%d\n", i);
    i++;
  }
  printf("%d\n", sum);
}
void Dowhile() {
  int i = 0, sum = 0;
  do {
    sum += i;
    i++;
  } while (i <= 100);
  printf("sum=%d", sum);
}
int main() {
  int a = 0;
  printf("������ѭ��������\n");
  scanf("%d", &a);
//whileѭ��
  Whileloop(a);
  Dowhile();
  return 0;
}