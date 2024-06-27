//
// Created by fuyunluochen on 2023/12/8.
//
#include <stdio.h>
void move(char start, char end, int n) {
  printf("��%d��Բ��:%c-->%c\n", n, start, end);
}
//a���Բ�̵ĳ�ʼ����,b��Ϊ�м����Ӵ��ʹ��,c���Ŀ������,nΪԲ�̵Ĳ���
void hanoi(char a, char b, char c, int n) {
  if (n == 1) {
    move(a, c, n);
  } else {
    hanoi(a, c, b, n - 1);
    move(a, c, n);
    hanoi(b, a, c, n - 1);
  }
}
int main() {
  hanoi('A', 'B', 'C', 3);
}
