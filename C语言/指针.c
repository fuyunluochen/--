//
// Created by fuyunluochen on 2023/12/12.
//
#include <stdio.h>

void pointer() {
  int a = 10;
  int *p = &a;
  printf("a���ڴ��еĵ�ַΪ:%p\n", p);
  printf("�ڴ�%p�洢��ֵΪ%d\n", p, *p);
  *p = 20;
  printf("ͨ��ָ���޸ĺ�%p��ֵΪ:%d", p, *p);

}

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

int main() {
  pointer();
  int a = 10, b = 20;
  printf("����ǰ:a=%d,b=%d\n", a, b);
  swap(&a, &b);
  printf("a = %d, b = %d\n", a, b);
  return 0;
}
