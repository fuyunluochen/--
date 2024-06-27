#include <stdio.h>

//@formatter:on
int main() {
  const double tomato_price = 1.3;
  const double cucumber_price = 2.5;
  const double potato_price = 1.2;
  float jin;
  scanf("%f", &jin);
  printf("%.2f\n", tomato_price * jin);
  printf("%.2f\n", cucumber_price * jin);
  printf("%.2f\n", potato_price * jin);
}