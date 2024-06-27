#include <stdio.h>

//@formatter:on
void GradeJudgment(int a) {
  if (a > 100 || a < 0) printf("输入错误");
  switch (a / 10) {
    case 10:
    case 9:printf("优秀\n");
      break;
    case 8:printf("良好\n");
      break;
    case 7:printf("中等\n");
      break;
    case 6:printf("及格\n");
      break;
    default:printf("不及格\n");
  }
}

int main() {
  int score = 0;
  while (1) {
    printf("请输入课程成绩(整数)：\n");
    scanf("%d", &score);
    GradeJudgment(score);
    if (score == -1) {
      return 0;

    }
  }
}