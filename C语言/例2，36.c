#include <stdio.h>
//@formatter:on
#define ZK1 9
#define ZK2 8
#define ZK3 0
#define CJ 65
int main() {
  float i = 10, j = 20, k = 30;
#ifdef ZK1
  printf("��Ʒ1�ļ۸�Ϊ=%.2f\n", i * ZK1 * 0.1);
#else
  printf("��Ʒ1�ļ۸�=%.2f\n",i);
#endif
#ifndef ZK2
  printf("��Ʒ2�ļ۸�=%.2f\n",j)
#else
  printf("��Ʒ2�ļ۸�=%.2f\n", j * ZK2 * 0.1);
#endif
#if (ZK3 > 0)
  printf("��Ʒ3�ļ۸�=%.2f\n", k * ZK3 * 0.1);
#else
  printf("��Ʒ3�ļ۸�=%.2f\n", k);
#endif
#if CJ >= 60 && CJ <= 100
  printf("�����ɼ�=%d,ͨ����\n", CJ);
#elif CJ >= 0 && cj <= 60
  printf("�����ɼ�=%d,��ͨ����\n",CJ);
#elif CJ<0&&CJ>100
  printf("�����ɼ�=%d,����\n",CJ);
#endif
  return 0;
}
