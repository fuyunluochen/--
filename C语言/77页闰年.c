#include <stdio.h>
//@formatter:on
int main() {
  int year;
  while (1) {
    printf("������������ݣ�(����0000�˳�)\n");
    scanf_s("%d", &year);
    if (year == 0000) {
      printf("���˳�");
      break;
    }
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
      printf("%d������\n", year);
    } else {
      printf("%d��������\n", year);
    }
  }
  return 0;
}