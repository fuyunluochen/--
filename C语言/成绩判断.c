#include <stdio.h>

//@formatter:on
void GradeJudgment(int a) {
  if (a > 100 || a < 0) printf("�������");
  switch (a / 10) {
    case 10:
    case 9:printf("����\n");
      break;
    case 8:printf("����\n");
      break;
    case 7:printf("�е�\n");
      break;
    case 6:printf("����\n");
      break;
    default:printf("������\n");
  }
}

int main() {
  int score = 0;
  while (1) {
    printf("������γ̳ɼ�(����)��\n");
    scanf("%d", &score);
    GradeJudgment(score);
    if (score == -1) {
      return 0;

    }
  }
}