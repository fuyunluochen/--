#include <stdio.h>
//@formatter:on
void two_dimensional_array() {
  int a[3][4];
  printf("������12��������\n");
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
      scanf("%d", &a[i][j]);
    }
  }
  char d;
  printf("��Ҫ��������𣿣�y/n��");
  scanf("%c", &d);
  if (d == 'y') {
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 4; j++) {
        printf("%3d", a[i][j]);
      }
    }
  }
  int max, row, col;
  max = a[0][0];
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 4; j++) {
      if (a[i][j] > max) {
        max = a[i][j];
        row = i;
        col = j;
      }
    }
  }
  printf("���ֵΪ:%d,��=%d,��=%d", max, row + 1, col + 1);
}
int main() {
  two_dimensional_array();
  return 0;
}