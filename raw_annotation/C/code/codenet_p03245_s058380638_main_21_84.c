#include <float.h>
#include <inttypes.h>
#include <limits.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <math.h>
#ifdef __cplusplus
#include <bits/stdc++.h>
#endif
#define getchar getchar
#define putchar putchar
int32_t nextint(void){ char c=getchar(); while(c!='-'&&(c<'0'||'9'<c)) c=getchar(); bool s=false; if(c=='-'){s=true;c=getchar();} uint32_t x=0; while('0'<=c && c<='9'){ x=x*10+c-'0'; c=getchar(); } return s?-x:x; }
int64_t nextlong(void){ char c=getchar(); while(c!='-'&&(c<'0'||'9'<c)) c=getchar(); int s=0; if(c=='-'){s=1;c=getchar();} uint64_t x=0; while('0'<=c && c<='9'){ x=x*10+c-'0'; c=getchar(); } return s?-x:x; }
uint32_t nextstr(char *s){ char c=getchar(); while(c==' '||c=='\n') c=getchar(); uint32_t len=0; while(c!=' '&&c!='\n'){ *s++=c; len++; c=getchar(); } *s='\0'; return len; }
int p[1000][2];
int main(void){
	int n=nextint();
	for(int i=0; i<n; i++){
		p[i][0]=nextint();
		p[i][1]=nextint();
	}
	int P=(p[0][0]^p[0][1])&1;
	for(int i=1; i<n; i++){
		if((p[i][0]^p[i][1]^P)&1){
			puts("-1");
			return 0;
		}
	}
	if(P){
		puts("31");
		puts("1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576 2097152 4194304 8388608 16777216 33554432 67108864 134217728 268435456 536870912 1073741824");
		const long s = 2147483647;
		for(int i=0; i<n; i++){
			long u = (s + p[i][0] + p[i][1])/2;
			long v = (s + p[i][0] - p[i][1])/2;
			for(int j=0; j<31; j++){
				if(u&(1<<j)){
					if(v&(1<<j)){
						putchar('R');
					}else{
						putchar('U');
					}
				}else{
					if(v&(1<<j)){
						putchar('D');
					}else{
						putchar('L');
					}
				}
			}
			putchar(10);
		}
	}else{
		puts("32");
		puts("1 1 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576 2097152 4194304 8388608 16777216 33554432 67108864 134217728 268435456 536870912 1073741824");
		const long s = 2147483647;
		for(int i=0; i<n; i++){
			long u = (s + p[i][0] + p[i][1] - 1)/2;
			long v = (s + p[i][0] - p[i][1] - 1)/2;
			putchar('R');
			for(int j=1; j<=31; j++){
				if(u&(1<<j)){
					if(v&(1<<j)){
						putchar('R');
					}else{
						putchar('U');
					}
				}else{
					if(v&(1<<j)){
						putchar('D');
					}else{
						putchar('L');
					}
				}
			}
			putchar(10);
		}
	}
}