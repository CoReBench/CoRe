#include <stdio.h>
#define inf 2e30+1
typedef long long ll;
int compare(const void *a, const void *b) {
  return *(int*)a - *(int*)b;
}
int main(void) {
  int i, j, k, n, m;
  scanf("%d%d", &n, &m);
  int x, y, uni[n], a[n];
  for(i = 0; i < n; ++i) 
    scanf("%d", &a[i]);
  for(i = 0; i < n; ++i) 
    uni[i] = i;
  for(i = 0; i < m; ++i) {
    scanf("%d%d", &x, &y);
    int t;
    if(uni[x] != x) {
      t = uni[y];
      uni[y] = x;
      for(j = y; uni[j] != j; ) {
        j = uni[j];
      }
      uni[y] = j;
      for(j = 0; j < n; ++j) {
        if(j == y) 
          continue;
        if(uni[j] == t) 
          uni[j] = uni[y];
      }
    } else {
      t = uni[x];
      uni[x] = y;
      for(j = x; uni[j] != j; ) {
        j = uni[j];
      }
      uni[x] = j;
      for(j = 0; j < n; ++j) {
        if(j == x) 
          continue;
        if(uni[j] == t) 
          uni[j] = uni[x];
      }
    }
  }
  int num = 0;
  for(i = 0; i < n; ++i) {
    if(uni[i] == i) 
      ++num;
  }
  if(num == 1) {
    printf("0");
    return 0;
  }
  if(num * 2 - 2 > n) {
    printf("Impossible");
    return 0;
  }
  if(num * 2 - 2 == n) {
    int t = 0;
    for(i = 0; i < n; ++i) 
      t += a[i];
    printf("%d", t);
    return 0;
  }
  int min[n], minn[n];
  for(i = 0; i < n; ++i) 
    min[i] = inf;
  for(i = 0; i < n; ++i) 
    if(min[uni[i]] > a[i]) {
      minn[uni[i]] = i;
      min[uni[i]] = a[i];
    }
  ll ssum = 0;
  int tnum = num - 2;
  for(i = 0; i < n; ++i) {
    int y = inf;
    if(min[i] != y) {
      ssum += (ll)min[i];
      a[minn[i]] = inf;
    }
  }
  qsort(a, n, sizeof(int), compare);
  for(i = 0; i < tnum; ++i) {
    ssum += a[i];
  }
  printf("%lld", ssum);
  return 0;
}