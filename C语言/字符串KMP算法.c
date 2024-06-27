#include <stdio.h>
#include <string.h>
int main() {
  char str1[] = "abababcabb";
  char str2[] = "ababc";
  int len1 = strlen(str1), len2 = strlen(str2);
  int next[len2];
  next[0] = 0;
  for (int i = 1; i < len2; i++) {
    int j = i - 1;
    while (1) {
      if (next[j] == 0 || str2[i - 1] == str2[next[j] - 1]) {
        next[i] = next[j] + 1;
        break;
      }
      j = next[j] - 1;
    }
  }
  for (int i = 0; i < len2 - 1; i++) {
    printf("%d ", next[i]);
  }
}