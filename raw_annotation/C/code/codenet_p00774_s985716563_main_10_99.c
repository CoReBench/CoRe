#include <stdio.h>
#include <stdlib.h>
int min(int a, int b){
  if (a > b) {
    return b;
  } else {
    return a;
  }
}
int main(void){
  int a[5][20];
  int b[5][10];
  int n,m;
  int point;
  scanf("%d",&n );
  while(n){
    point = 0;
    for (int i = 0; i < 20; i++) {
      for (int j = 0; j < 5; j++) {
        a[j][i] = 0;
      }
    }
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < 5; j++) {
        scanf("%d",&a[j][n-1-i] );
      }
    }
    m = 11;
    while(m > 0){
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < 5; j++) {
          b[j][i] = 0;
        }
      }
      for (int i = 0; i < n; i++) {
        if (a[0][i] == a[1][i] && a[1][i] == a[2][i] && a[0][i] != 0) {
          if (a[2][i] == a[3][i]) {
            if (a[3][i] == a[4][i]) {
              point += a[0][i] * 5;
              for (int j = 0; j < 5; j++) {
                b[j][i] = 1;
              }
            }else{
              point += a[0][i] * 4;
              for (int j = 0; j < 4; j++) {
                b[j][i] = 1;
              }
            } 
          }else{
              point += a[0][i] * 3;
              for (int j = 0; j < 3; j++) {
                  b[j][i] = 1;
              }
            }
        }else if (a[1][i] == a[2][i] && a[2][i] == a[3][i] && a[1][i] != 0) {
          if (a[3][i] == a[4][i]) {
            point += a[1][i] * 4;
            for (int j = 1; j < 5; j++) {
              b[j][i] = 1;
            }
          }else{
            point += a[1][i] * 3;
            for (int j = 1; j < 4; j++) {
              b[j][i] = 1;
            }
          }
        }else if (a[2][i] == a[3][i] && a[3][i] == a[4][i] && a[2][i] != 0) {
          point += a[2][i] * 3;
          for (int j = 2; j < 5; j++) {
            b[j][i] = 1;
          }
        }
      }
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < 5; j++) {
          if (b[j][i] == 1) {
            a[j][i] = 0;
            b[j][i] = 0;
          }
        }
      }
      for (int e = 0; e < n; e++) {
        for (int i = 0; i < n; i++) {
          for (int j = 0; j < 5; j++) {
            if (a[j][i] == 0) {
              for (int l = i; l < 10; l++) {
                a[j][l] = a[j][l+1];
              }
            }
          }
        }
      }
      m--;
    }
    printf("%d\n",point );
    scanf("%d",&n );
  }
  return 0;
}