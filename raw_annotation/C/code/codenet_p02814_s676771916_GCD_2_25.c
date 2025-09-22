#include <stdio.h>
long GCD(long a, long b){
  long dividend, divisor;
  if (a >= b) {
    dividend = a;
    divisor = b;
  } else {
    dividend = b;
    divisor = a;
  }
  long remainder;
  while (1) {
    if (divisor == 1) {
      return 1;
    }
    remainder = dividend % divisor;
    if (remainder == 0) {
      break;
    } else {
      dividend = divisor;
      divisor = remainder;
    }
  }
  return divisor;
}
int main(void) {
  long n,m;
  scanf("%ld %ld", &n, &m);
  long a[n];
  for (long i = 0; i < n; i++) {
    scanf("%ld", &a[i]);
  }
  long lcm_all = a[0];
  for (long i = 1; i < n; i++) {
    lcm_all = (lcm_all/GCD(lcm_all,a[i]))*a[i];
    if (lcm_all > 3000000000) {
      lcm_all = 3000000000;
    }
  }
  long half = lcm_all/2;
  for (long i = 0; i < n; i++) {
    if (half%a[i] != a[i]/2) {
      printf("0\n");
      return 0;
    }
  }
  long mod = m%lcm_all;
  long ans = m/lcm_all;
  if (mod >= half) {
    ans++;
  }
  printf("%ld\n", ans);
  return 0;
}