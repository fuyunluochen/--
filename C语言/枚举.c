// #include <stdio.h>
// enum Day{
//   Mon=1,Tue,Wed,Thu,Fri,Sat,Sun
// } day;
// int main(){
//   enum Day day;
//   day =Wed;
//   printf("%d\n",day);
////  遍历Day
//  for (day = Mon;  day<=Sun ; day++) {
//    printf("枚举元素：%d\n",day);
//  }
//  return 0;
//}
#include <stdio.h>
#include <stdlib.h>
int main() {
  enum color { red=1, green, blue };
  enum color favorite_color;
  printf("请输入您喜欢的颜色：(1.red,2.green,3.blue)");
  scanf_s("%u", &favorite_color);
  switch (favorite_color) {
    case red:
      printf("您喜欢的是红色");
      break;
    case green:
      printf("您喜欢的是绿色");
      break;
    case blue:
      printf("您喜欢的是蓝色");
      break;
    default:
      printf("没有您喜欢的颜色");
      break;
  }
}