//
// Created by fuyunluochen on 2023/12/12.
//
#include <stdio.h>

void pointer() {
  int a = 10;
  int *p = &a;
  printf("a在内存中的地址为:%p\n", p);
  printf("内存%p存储的值为%d\n", p, *p);
  *p = 20;
  printf("通过指针修改后%p的值为:%d", p, *p);

}

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

int main() {
  pointer();
  int a = 10, b = 20;
  printf("互换前:a=%d,b=%d\n", a, b);
  swap(&a, &b);
  printf("a = %d, b = %d\n", a, b);
  return 0;
}
