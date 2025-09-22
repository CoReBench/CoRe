#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int descending_compare(const void *a, const void *b){
    if (*(int*)a > *(int*)b){
        return -1;
    }else if (*(int*)a == *(int*)b){
        return 0;
    }else{
        return 1;
    }
}
int ascending_compare(const void *a, const void *b){
    if (*(int*)a < *(int*)b){
        return -1;
    }else if (*(int*)a == *(int*)b){
        return 0;
    }else{
        return 1;
    }
}
int lower_bound(int *a, int n, int key){
    int left, mid, right;
    left = 0, right = n;
    mid = (left + right)/2;
    while ((left+1 != mid || mid+1 != right) && mid != left){
        if (key > a[mid]){
            left = mid;
        }else{
            right = mid+1;
        }
        mid = (left + right)/2;
    }
    if (a[left] >= key)return left;
    if (a[mid] >= key)return mid;
    if (a[right] >= key)return right;
    return n;
}
unsigned long  gcd(unsigned long x, unsigned long y){
    if (y == 0){ 
        return x;
    }else if (x > y){
        return gcd(y, x % y);
    }else{
        return gcd(x, y % x);
    }
}
long long factorial(int x){
    long long rtn = 1;
    int i;
    for (i = x; i > 1; i--){
        rtn = (rtn*i);
    }
    return rtn;
}
int main(void){
    int h, w;
    long long square[3];
    long long min, max;
    long long ans = 10000000000000;
    scanf("%d %d", &h, &w);
    for (int i = 1; i < h; i++){
        square[0] = (long long)i * w;
        square[1] = (long long)(h-i)*(w/2);
        square[2] = (long long)(h-i)*(w-w/2);
        min = 10000000000000, max = 0;
        for (int j = 0; j < 3; j++){
            if (min > square[j]){
                min = square[j];
            }
            if (max < square[j]){
                max = square[j];
            }
        }
        if (ans > llabs(max-min)){
            ans = llabs(max-min);
        }
        square[1] = (long long)(h-i)/2*w;
        square[2] = (long long)((h-i)-(h-i)/2)*w;
        min = 10000000000000, max = 0;
        for (int j = 0; j < 3; j++){
            if (min > square[j]){
                min = (long long)square[j];
            }
            if (max < square[j]){
                max = (long long)square[j];
            }
        }
        if (ans > llabs(max-min)){
            ans = llabs(max-min);
        }
    }
    for (int i = 0; i < w; i++){
        square[0] = (long long)i*h;
        square[1] = (long long)(w-i)*(h/2);
        square[2] = (long long)(w-i)*(h-h/2);
        min = 10000000000000, max = 0;
        for (int j = 0; j < 3; j++){
            if (min > square[j]){
                min = (long long)square[j];
            }
            if (max < square[j]){
                max = (long long)square[j];
            }
        }
        if (ans > llabs(max-min)){
            ans = llabs(max-min);
        }
        square[1] = (long long)(w-i)/2*h;
        square[2] = (long long)((w-i)-(w-i)/2)*h;
        min = 10000000000000, max = 0;
        for (int j = 0; j < 3; j++){
            if (min > square[j]){
                min = (long long)square[j];
            }
            if (max < square[j]){
                max = (long long)square[j];
            }
        }
        if (ans > llabs(max-min)){
            ans = llabs(max-min);
        }
    }
    printf("%lld\n", ans);
    return 0;
}