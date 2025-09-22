#include <stdio.h>
#include <stdlib.h>
#define MAXS 10005
long int getmax(long int a, long int b);
int main(int argc, char *argv[]) {
	int ntests;
	scanf("%d", &ntests);
	int test;
	long int D[MAXS];
	long int A[MAXS];
	long int B[MAXS];
	long int M[MAXS], N[MAXS];
	int longm[MAXS], longn[MAXS];
	int s;
	int i;
	int j;
	int max;
	int max_no;
	for (test=1; test<=ntests; test++) {
		scanf("%d", &s);
		for (i=0; i<s; i++) {
			scanf("%li %li %li", D+i, A+i, B+i);
			M[i] = D[i]+A[i];
			N[i] = D[i] - B[i];
		}
		longm[0] = 1;
		longn[0] = 1;
		for (i=1; i<s; i++) {
			if (M[i] ==M[i-1]) {
				longm[i] = longm[i-1] + 1;
			}
			else {
				longm[i] = 2;
				j=i-2;
				while (j>=0 && (M[j]==M[i] || N[j]==N[i-1])) {
					longm[i]++;
					j--;
				}
			}
			if (N[i] ==N[i-1]) {
				longn[i] = longn[i-1] + 1;
			}
			else {
				longn[i] = 2;
				j=i-2;
				while (j>=0 && (N[j]==N[i] || M[j]==M[i-1])) {
					longn[i]++;
					j--;
				}
			}
		}
		max = getmax(longm[0], longn[0]);
		max_no = 1;
		for (i=1; i<s; i++) {
			if (getmax(longm[i], longn[i]) > max) {
				max_no = 1;
				max = getmax(longm[i], longn[i]);
			}
			else if (getmax(longm[i], longn[i]) == max) {
				max_no++;
			}
		}
		printf("Case #%d: %d %d\n", test, max, max_no);
	}
	return 0;
}
long int getmax(long int a, long int b) {
	if (a>b) {
		return a;
	}
	return b;
}