#include <stdio.h>
#include <stdlib.h>
int int_sort( const void * a , const void * b ) {
  if( *(int*)a < *(int*)b ) {
    return -1;
  } else if( *(int*)a == *(int*)b ) {
    return 0;
  }
  return 1;
}
int main(void) {
  int N;
  scanf("%d", &N);
  int A[100000];
  for(int i = 0; i < N; i++) {
    scanf("%d", &A[i]);
  }
  if(N == 2) {
    printf("%d\n", abs(A[0] - A[1]));
    return 0;
  }
  qsort((void*)A, N, sizeof(A[0]), int_sort);
  int B[100000];
  int pos = N / 2;
  int beg, end;
  int flag;
  int offset;
  B[pos] = A[0];
  beg = 1;
  end = N - 1;
  flag = 1;
  offset = 1;
  while(1) {
    if(flag == 1) {
      B[pos-offset] = A[end--];
      if(end < beg) break;
      B[pos+offset] = A[end--];
      if(end < beg) break;
      flag = 0;
    } else {
      B[pos-offset] = A[beg++];
      if(end < beg) break;
      B[pos+offset] = A[beg++];
      if(end < beg) break;
      flag = 1;
    }
    offset++;
  }
  int C[100000];
  C[pos] = A[N-1];
  beg = 0;
  end = N - 2;
  flag = 0;
  offset = 1;
  while(1) {
    if(flag == 1) {
      C[pos-offset] = A[end--];
      if(end < beg) break;
      C[pos+offset] = A[end--];
      if(end < beg) break;
      flag = 0;
    } else {
      C[pos-offset] = A[beg++];
      if(end < beg) break;
      C[pos+offset] = A[beg++];
      if(end < beg) break;
      flag = 1;
    }
    offset++;
  }
  long long int sumB = 0;
  for(int i = 1; i < N; i++) {
    sumB += abs(B[i-1] - B[i]);
  }
  long long int sumC = 0;
  for(int i = 1; i < N; i++) {
    sumC += abs(C[i-1] - C[i]);
  }
#if 0
  printf("B[]=");
  for(int i = 0; i < N; i++) {
    printf("%d ", B[i]);
  }
  printf(": sum=%lld\n", sumB);
  printf("C[]=");
  for(int i = 0; i < N; i++) {
    printf("%d ", C[i]);
  }
  printf(": sum=%lld\n", sumC);
#endif
  if(sumB < sumC)
    printf("%lld\n", sumC);
  else
    printf("%lld\n", sumB);
  return 0;
}