#include <stdio.h>
//@formatter:on
int main() {
  float money;
  printf("请输入购物金额：\n");
  while (1) {
    scanf("%f", &money);
    if (money >= 1000)
      printf("打折后购物价格为：%.2f\n", money * 0.8);
    else if (money >= 500)
      printf("打折后购物价格为：%.2f\n", money * 0.9);
    else if (money >= 200)
      printf("打折后购物价格为：%.2f\n", money * 0.95);
    else if (money >= 100)
      printf("打折后购物价格为：%.2f\n", money * 0.97);
    else if (money >= 0)
      printf("购物价格为：%.2f\n", money);
    else if (money < 0)
      printf("输入错误，请重新输入！\n");
    if (money == -1) {
      break;
    }
  }
  return 0;
}