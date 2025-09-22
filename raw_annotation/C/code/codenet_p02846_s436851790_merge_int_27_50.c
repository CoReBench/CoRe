#include <stdio.h>
#define NDEBUG
#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#ifdef NDEBUG
#define DEBUG_PRINT(fmt, ...) ((void)0)
#else
#define DEBUG_PRINT(fmt, ...) fprintf(stderr, fmt, ##__VA_ARGS__)
#endif
#define ASSERT_RANGE(min,x,max) assert(((x)>=(min)) && ((x)<=(max)))
int sort_int(int *a, int N) {
	int i;
	for (i = 0; i < N-1; i++) {
		int j;
		for (j = i + 1; j < N; j++) {
			if (a[i] > a[j]) {
				int tmp = a[i];
				a[i] = a[j];
				a[j] = tmp;
			}
		}
	}
	return 0;
}
void merge_int(int *a, int *b, int lower, int sep, int upper) {
	int i_lower = lower;
	int i_upper = sep;
	int i_b = 0;
	while ((i_lower < sep) && (i_upper < upper)) {
		if (a[i_lower] < a[i_upper]) {
			b[i_b++] = a[i_lower++];
		} else {
			b[i_b++] = a[i_upper++];
		}
	}
	if (i_lower >= sep) {
		while (i_upper < upper) {
			b[i_b++] = a[i_upper++];
		}
	} else {
		while (i_lower < sep) {
			b[i_b++] = a[i_lower++];
		}
	}
	for (i_lower = 0; i_lower < i_b; i_lower++) {
		a[i_lower+lower] = b[i_lower];
	}
}
void merge_sort_int(int *a, int *b, int lower, int upper) {
	int sep;
	if ((lower == upper) || (lower + 1 == upper)) {
		return;
	}
	sep = (lower + upper) / 2;
	merge_sort_int(a,b,lower,sep);
	merge_sort_int(a,b,sep,upper);
	merge_int(a,b,lower,sep,upper);
}
#define S_MAX 30000
int main(int argc, char **argv) {
	long long t1, t2;
	long long a1, a2;
	long long b1, b2;
	fscanf(stdin,"%lld%lld",&t1,&t2) > 0;
	fscanf(stdin,"%lld%lld",&a1,&a2) > 0;
	fscanf(stdin,"%lld%lld",&b1,&b2) > 0;
	long long diff1 = (a1-b1)*t1;
	long long diff2 = (a2-b2)*t2;
	long long diff3 = diff1 + diff2;
	DEBUG_PRINT("%lld %lld %lld\n",diff1, diff2, diff3);
	if ((diff1 > 0) && (diff2 > 0)) {
		fprintf(stdout,"0\n");
		return 0;
	}
	if ((diff1 < 0) && (diff2 < 0)) {
		fprintf(stdout,"0\n");
		return 0;
	}
	if ((diff1 > 0) && (diff2 < 0)) {
		if (diff3 > 0) {
			fprintf(stdout,"0\n");
			return 0;
		}
		if (diff3 == 0) {
			fprintf(stdout,"infinity\n");
			return 0;
		}
		assert(diff3 < 0);
		long long  n = diff1 / llabs(diff3);
		if ((diff1 * n) == llabs(diff3)) {
			fprintf(stdout,"%lld\n",2*n);
		} else {
			fprintf(stdout,"%lld\n",1+2*n);
		}
		return 0;
	}
	if ((diff1 < 0) && (diff2 > 0)) {
		if (diff3 < 0) {
			fprintf(stdout,"0\n");
			return 0;
		}
		if (diff3 == 0) {
			fprintf(stdout,"infinity\n");
			return 0;
		}
		assert(diff3 > 0);
		long long n = llabs(diff1) / diff3;
		if ((llabs(diff1) * n) == diff3) {
			fprintf(stdout,"%lld\n",2*n);
		} else {
			fprintf(stdout,"%lld\n",1+2*n);
		}
		return 0;
	}
	return 0;
}