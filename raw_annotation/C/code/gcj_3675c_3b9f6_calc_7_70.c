#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
void calc()
{
  int M, S = 0, R = 0;
  scanf("%d", &M);
  int* r1 = (int*) malloc(sizeof(int) * M);
  int* r2 = (int*) malloc(sizeof(int) * M);
  for (int i = 0; i < M; i++)
  {
    scanf("%d %d", &r1[i], &r2[i]);
    r1[i]--;
    r2[i]--;
  }
  long long* G = (long long*) malloc(sizeof(long long) * M);
  long long* f = (long long*) malloc(sizeof(long long) * M);
  for (int i = 0; i < M; i++)
  {
    scanf("%lld", &G[i]);
    f[i] = 0;
    S += G[i];
  }
  f[0] = 1;
  int g, s = 1;
  while (s <= S)
  {
    int n = INT_MAX;
    for (int j = 0; j < M; j++)
      if (f[j] > 0)
      {
        n = MIN(n, G[j] / f[j]);
        g = j;
      };
    if (n > 0)
    {
      R += n;
      for (int j = 0; j < M; j++)
        if (f[j] > 0)
        {
          G[j] -= f[j] * n;
          S -= f[j] * n;
        }
    }
    G[r1[g]] += G[g];
    G[r2[g]] += G[g];
    long long a = f[g];
    s += a;
    if (s > S)
    {
      free(f);
      free(G);
      free(r2);
      free(r1);
      printf("%d\n", R);
      return;
    }
    f[g] = 0;
    f[r1[g]] += a;
    f[r2[g]] += a;
  }
  free(f);
  free(G);
  free(r2);
  free(r1);
  printf("%d\n", R);
}
int main(void)
{
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++)
  {
    printf("Case #%d: ", t);
    calc();
  }
  return EXIT_SUCCESS;
}