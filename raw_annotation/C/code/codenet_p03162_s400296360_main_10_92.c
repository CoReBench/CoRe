#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int max1(int a, int b) {
	if (a > b)
		return a;
	else
		return b;
}
int main()
{
	int N = 0;
	int *A,*B,*C;
	int SUM = 0;
	int sumA = 0, sumB = 0, sumC = 0;
	char ref = 0;
	int N_limit = pow(10, 5);
	if (scanf("%d", &N) <= 0) {
		exit(1);
	}
	if ( N <= 0 || N_limit < N)
		exit(1);
	A = (int *)malloc(N * sizeof(int));
	B = (int *)malloc(N * sizeof(int));
	C = (int *)malloc(N * sizeof(int));
	for (int i = 0; i < N; i++)
	{
		if (scanf("%d%d%d", &A[i], &B[i], &C[i]) < 3) {
			exit(1);
		}
		if (A[i] <= 0 || pow(10, 4) < A[i])
			exit(1);
		else if (B[i] <= 0 || pow(10, 4) < B[i])
			exit(1);
		else if (C[i] <= 0 || pow(10, 4) < C[i])
			exit(1);
	}
	int ref_A = 0, ref_B = 0, ref_C = 0;
	for (int i = 0; i < N; i++)
	{
		if (i - 1 <= 0)
		{
			sumA = A[i];
			sumB = B[i];
			sumC = C[i];
			ref_A = sumA;
			ref_B = sumB;
			ref_C = sumC;
			continue;
		}
		sumA = A[i] + max1(ref_B, ref_C);
		sumB = B[i]+ max1(ref_C, ref_A);
		sumC = C[i] + max1(ref_A, ref_B);
		ref_A = sumA;
		ref_B = sumB;
		ref_C = sumC;
	}
	if (sumA >= sumB)
	{
		if (sumA >= sumC)
		{
			SUM = sumA;
		}
		else
		{
			SUM = sumC;
		}
	}
	else if (sumB >= sumA)
	{
		if (sumB >= sumC)
		{
			SUM = sumB;
		}
		else
		{
			SUM = sumC;
		}
	}
	else if (sumC >= sumB)
	{
		if (sumC >= sumA)
		{
			SUM = sumC;
		}
		else
		{
			SUM = sumA;
		}
	}
	printf("%d", SUM);
}