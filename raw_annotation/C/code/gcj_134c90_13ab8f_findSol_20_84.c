#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void findSol(char** C, int A, int i);
int main(int argc, char *argv[]) {
	int T, A;
	scanf("%d", &T);
	for (int i=0; i<T; i++) {
		scanf("%d", &A);
		char **C;
		C = (char**) calloc(A, sizeof(char*));
		for (int j=0; j<A; j++) {
			 C[j] = (char *) calloc(501, sizeof(char));
			 scanf("%s", C[j]);
		}
		findSol(C, A, i+1);
	}
	return 0;
}
void findSol(char** C, int A, int T) {
	printf("Case #%d: ", T);
	char S[501], L;
	int X[3] = {0, 0, 0}, noSol=0, n=0, haveWon = 1;
	int *count;
	count = (int*) calloc(A, sizeof(int));
	while (1) {
		for (int i=0; i<A; i++) {
			if ( count[i] == -1 ) {
				continue;
			}
			haveWon=0;
			if ( C[i][count[i]] == '\0' ) {
				count[i] = 0;
			}
			if ( C[i][count[i]] == 'R' ) {
				X[0] = 1;
			} else if ( C[i][count[i]] == 'P' ) {
				X[1] = 1;
			} else {
				X[2] = 1;
			}
			if ( X[0] == 1 && X[1] == 1 && X[2] == 1 ) {
				noSol = 1;
				break;
			}
		}
		if (noSol || n > 500) {
			printf("IMPOSSIBLE\n");
			return;
		}
		if (haveWon) {
			S[n] = '\0';
			printf("%s\n", S);
			return;
		}
		if (X[0]) {
			if (X[2]) {
				S[n] = 'R';
				L = 'S';
			} else {
				S[n] = 'P';
				L = 'R';
			}
		} else {
			if (X[1]) {
				S[n] = 'S';
				L = 'P';
			} else {
				S[n] = 'R';
				L = 'S';
			}
		}
		for (int j=0; j<A; j++) {
			if ( count[j] == -1 || C[j][count[j]] == L) {
				count[j] = -1;
				continue;
			}
			count[j]++;
		}
		X[0] = 0; X[1] = 0; X[2] = 0;
		n++;
		haveWon = 1;
	}
}