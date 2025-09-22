#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define sl(x) scanf("%ld", &x)
#define ss(x) scanf("%s", x)
#define pl(x) printf("%ld\n", x)
#define pd(x) printf("%lf\n", x)
#define ps(x) printf("%s\n", x)
#define INF 1000000000000000000
#define MOD 1000000007
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
int compare_long(const void *a, const void *b) {
	return *(long*)a - *(long*)b;
}
int main() {
	long N, M;
	long a[300001];
	char s[100010];
	long i, j;
	char ans[100010];
	long pre, next;
	scanf("%ld", &N);
	scanf("%s", s);
	for(i=0;i<N;i++) 
		ans[i] = 'S';
	ans[N] = '\0';
	for(i=0;i<N-1;i++) {
		pre = (i + N - 1) % N;
		next = (i + 1) % N;
		if(ans[i] == 'S') {
			if(s[i] == 'o' && ans[pre] != ans[next]) {
				ans[next] = ans[pre];
			}
			if(s[i] == 'x' && ans[pre] == ans[next]) {
				ans[next] = ans[next] == 'S' ? 'W' : 'S';
			}
		} else {
			if(s[i] == 'o' && ans[pre] == ans[next]) {
				ans[next] = ans[next] == 'S' ? 'W' : 'S';
			}
			if(s[i] == 'x' && ans[pre] != ans[next]) {
				ans[next] = ans[pre];
			}
		}
	}
	if(ans[N-1] == 'S') {
		if(s[N-1] == 'o' && ans[N-2] == ans[0]) {
			printf("%s\n", ans);
			return 0;
		}
		if(s[N-1] == 'x' && ans[N-2] != ans[0]) {
			printf("%s\n", ans);
			return 0;
		}
	} else {
		if(s[N-1] == 'o' && ans[N-2] != ans[0]) {
			printf("%s\n", ans);
			return 0;
		}
		if(s[N-1] == 'x' && ans[N-2] == ans[0]) {
			printf("%s\n", ans);
			return 0;
		}
	}
	for(i=0;i<N;i++) 
		ans[i] = 'W';
	ans[N] = '\0';
	for(i=0;i<N-1;i++) {
		pre = (i + N - 1) % N;
		next = (i + 1) % N;
		if(ans[i] == 'S') {
			if(s[i] == 'o' && ans[pre] != ans[next]) {
				ans[next] = ans[pre];
			}
			if(s[i] == 'x' && ans[pre] == ans[next]) {
				ans[next] = ans[next] == 'S' ? 'W' : 'S';
			}
		} else {
			if(s[i] == 'o' && ans[pre] == ans[next]) {
				ans[next] = ans[next] == 'S' ? 'W' : 'S';
			}
			if(s[i] == 'x' && ans[pre] != ans[next]) {
				ans[next] = ans[pre];
			}
		}
	}
	if(ans[N-1] == 'S') {
		if(s[N-1] == 'o' && ans[N-2] == ans[0]) {
			printf("%s\n", ans);
			return 0;
		}
		if(s[N-1] == 'x' && ans[N-2] != ans[0]) {
			printf("%s\n", ans);
			return 0;
		}
	} else {
		if(s[N-1] == 'o' && ans[N-2] != ans[0]) {
			printf("%s\n", ans);
			return 0;
		}
		if(s[N-1] == 'x' && ans[N-2] == ans[0]) {
			printf("%s\n", ans);
			return 0;
		}
	}
	ps("-1");
	return 0;
}