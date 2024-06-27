#include <stdio.h>
//@formatter:on
#define ZK1 9
#define ZK2 8
#define ZK3 0
#define CJ 65
int main() {
  float i = 10, j = 20, k = 30;
#ifdef ZK1
  printf("商品1的价格为=%.2f\n", i * ZK1 * 0.1);
#else
  printf("商品1的价格=%.2f\n",i);
#endif
#ifndef ZK2
  printf("商品2的价格=%.2f\n",j)
#else
  printf("商品2的价格=%.2f\n", j * ZK2 * 0.1);
#endif
#if (ZK3 > 0)
  printf("商品3的价格=%.2f\n", k * ZK3 * 0.1);
#else
  printf("商品3的价格=%.2f\n", k);
#endif
#if CJ >= 60 && CJ <= 100
  printf("考生成绩=%d,通过！\n", CJ);
#elif CJ >= 0 && cj <= 60
  printf("考生成绩=%d,不通过！\n",CJ);
#elif CJ<0&&CJ>100
  printf("考生成绩=%d,错误！\n",CJ);
#endif
  return 0;
}
