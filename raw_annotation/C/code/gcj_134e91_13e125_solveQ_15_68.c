#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
void solveQ(int F);
int main(int argc, char *argv[]) {
	int T, F;
	scanf("%d", &T);
	scanf("%d", &F);
	for (int i=0; i<T; i++) {
		solveQ(F);
	}
	return 0;
}
void solveQ(int F) {
	char S[6], l;
	int C[5] = {0, 0, 0, 0, 0};
	int n = 0, x, hasLet=0, letter;
	for (int d = 1; d<=5; d++) {
		for (int i=0; i<119; i++) {
			for (int j=0; j<5; j++) {
				if (hasLet > 1) {
					break;
				}
				if ( C[j] < 24 ) {
					hasLet++;
					letter = j;
				}
			}
			if (hasLet > 1) {
				hasLet = 0;
			} else {
				hasLet = 0;
				S[d-1] = 'A' + letter;
				C[0] = 0; C[1] = 0; C[2] = 0; C[3] = 0; C[4] = 0;
				if (d == 5) {
					break;
				}
				for (int k = d-1; d>=0; d--) {
					C[S[k]-'A'] = 24;
				}
				break;
			}
			x = 5*i + d;
			printf("%d\n", x);
			fflush(stdout);
			scanf("%c", &l);
			C[l - 'A']++;
			for (int j=0; j<5; j++) {
				if (hasLet > 1) {
					break;
				}
				if ( C[j] < 24 ) {
					hasLet++;
				}
			}
		}
	}
	S[5] = '\0';
	printf("%s\n", S);
	fflush(stdout);
	scanf("%c", &l);
	if (l == 'Y') {
		return;
	} else {
		exit(0);
	}
}