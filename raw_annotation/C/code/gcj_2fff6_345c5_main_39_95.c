#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int A[101][101];
int B[101][101];
int r, c, h, v;
int guests, chips, share;
int fr(int rRemaining, int i, int j) {
	int k;
	if( (rRemaining + 1)*share != (B[r][j] - B[i][j]) )
		return 0;
	if(rRemaining == 0) 
		return 1;
	k = i+1;
	while(k < r) {
		if(B[k][j] - B[i][j] == share) {
			return fr(rRemaining - 1, k, j);
		}
		k++;
	}
	return 0;
}
int fc(int cRemaining, int i, int j) {
	int k;
	if( (cRemaining + 1)*share != (B[i][c] - B[i][j]) )
		return 0;
	if(cRemaining == 0) 
		return 1;
	k = i+1;
	while(k < c) {
		if(B[i][k] - B[i][j] == share) {
			return fr(cRemaining - 1, i, k);
		}
		k++;
	}
	return 0;
}
int main() {
	int t, tc;
	int i, j, possible;
	char str[101];
	scanf("%d", &t);
	tc = 1;
	while(tc <= t) {
		scanf("%d", &r);
		scanf("%d", &c);
		scanf("%d", &h);
		scanf("%d", &v);
		guests = (h+1)*(v+1);
		chips = 0;
		for (i = 0; i <= r; ++i) {
			if(i != 0) scanf("%s", str);
			for (j = 0; j <= c; ++j) {
				if(i == 0 || j == 0) 
					A[i][j] = B[i][j] = 0;
				else {
					A[i][j] = (str[j-1] == '@') ? 1 : 0; 
					if(A[i][j]) 
						chips++;
				}
			}
		}
		if(chips % guests != 0) {
			printf("Case #%d: IMPOSSIBLE\n", tc);
		} else {
			for (i = 1; i <= r; ++i) {
				for (j = 1; j <= c; ++j) {
					B[i][j] = A[i][j] + B[i-1][j] + B[i][j-1] - B[i-1][j-1];
				}
			}
			share = chips / guests;
			possible = 0;
			for (i = 1; i < r && !possible; ++i) {
				for (j = 1; j < c && !possible; ++j) {
					if(B[i][j] == share) {
						possible = 1;
						if(!fr(h - 1, i, j)) {
							possible = 0;
						}
						if(!fc(v - 1, i, j)) {
							possible = 0;
						}
						if(possible) {
							printf("Case #%d: POSSIBLE\n", tc);
						}
					}
				}
			}
			if(!possible) printf("Case #%d: IMPOSSIBLE\n", tc);
		}
		tc++;
	}
	return 0;
}