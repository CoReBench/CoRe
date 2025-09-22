#ifndef _GNU_SOURCE
#define _GNU_SOURCE
#endif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <ctype.h>
#include <stdarg.h>
#include <math.h>
static int dpr (const char *fmt, ...)
{
  int res = 0;
  va_list ap;
  va_start (ap, fmt);
#if 0
  res = vprintf (fmt, ap);
#endif
  va_end (ap);
  return res;
}
int main ()
{
  int T;
  scanf ("%d\n", &T);
  for (int i = 0; i < T; i++)
    {
      int N, P;
      scanf ("%d %d\n", &N, &P);
      int P_orig = P;
      int *w = (int *)malloc (sizeof (int) * N);
      int *h = (int *)malloc (sizeof (int) * N);
      int *min_add = (int *)malloc (sizeof (int) * N);
      double *max_add = (double *)malloc (sizeof (double) * N);
      double *best_min = (double *)malloc (sizeof (double) * N);
      double *best_max = (double *)malloc (sizeof (double) * N);
      double total = 0;
      for (int j = 0; j < N; j++)
        {
          scanf ("%d %d\n", w + j, h + j);
          int circ = (w[j] + h[j]) * 2;
          P -= circ;
          total += circ;
          min_add[j] = 2 * (w[j] < h[j] ? w[j] : h[j]);
          max_add[j] = 2 * sqrt (w[j] * w[j] + h[j] * h[j]);
        }
      dpr ("looking for %d\n", P);
      double best_valid = 0;
      for (int j = 0; j < N; j++)
        {
          int min1 = 0;
          int max1 = 0;
          int k1 = -1;
          for (int k = 0; k < j; k++)
            if (best_min[k] + min_add[j] < P && best_max[k] > max1) {
              k1 = k;
              min1 = best_min[k];
              max1 = best_max[k];
            }
          best_min[j] = min1 + min_add[j];
          best_max[j] = max1 + max_add[j];
          dpr ("cookie %d: using prev %d [%f..%f]\n", j, k1, best_min[j], best_max[j]);
          if (best_min[j] <= P && best_max[j] > best_valid)
            best_valid = best_max[j];
        }
      if (best_valid > P)
	      best_valid = P;
      printf ("Case #%d: %.6f\n", i + 1, total + best_valid);
      free (max_add);
      free (min_add);
      free (h);
      free (w);
    }
  exit (0);
}