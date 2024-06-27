//
// Created by fuyunluochen on 2023/12/8.
//
#include <stdio.h>
void move(char start, char end, int n) {
  printf("第%d个圆盘:%c-->%c\n", n, start, end);
}
//a存放圆盘的初始柱子,b作为中间柱子存放使用,c存放目标柱子,n为圆盘的层数
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
