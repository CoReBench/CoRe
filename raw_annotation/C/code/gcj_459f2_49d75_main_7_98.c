#include <stdio.h>
int A[1005];
int ori[1005];
char res[1005][1005];
int cnt[1005][1005];
int max(int a, int b){ return a > b ? a : b; }
int main(){
    int T;
    scanf("%d", &T);
    for(int tc=0; tc<T; tc++){
        int C;
        scanf("%d", &C);
        for(int i=1; i<=C; i++) {
            scanf("%d", &A[i]);
            ori[i] = A[i];
        }
        int mx = 0;
        for(int i=1; i<=C; i++) 
            mx = max(mx, A[i]);
        printf("Case #%d: ", tc+1);
        if(A[1] == 0 || A[C] == 0){
            printf("IMPOSSIBLE\n");
            continue;
        }
        int R = 0;
        for(int i=1; i<=C; i++) 
            for(int j=1; j<=C; j++) 
                res[i][j] = '.';
        int cur = 0;
        int cons = 0;
        for(int i=1; i<=C; i++){
            if(cur >= 1){
                int fi = 0;
                for(int j=1; j<C; j++) 
                    if(A[j]){
                        fi = j;
                        break;
                    }
                for(int j=i; j>fi; j--){
                    res[i-j+1][j] = '/';
                    R = max(R, i-j+1);
                }
                A[fi]--;
                cur--;
                cur += A[i];
                cons = 0;
            } else{
                cur += A[i];
                if(cur >= 1){
                    cur--;
                    A[i] = cur;
                    cons = 0;
                } else{
                    cons++;
                    for(int j=1; j<=-cur+1; j++) 
                        res[j][i] = '\\';
                    R = max(R, -cur+1);
                    cur--;
                }
            }
        }
        for(int i=1; i<=R+1; i++) 
            for(int j=1; j<=C; j++)
                cnt[i][j] = 0;
        for(int i=1; i<=C; i++) 
            cnt[1][i] = 1;
        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++){
                if(res[i][j] == '.') 
                    cnt[i+1][j] += cnt[i][j];
                else if(res[i][j] == '\\') 
                    cnt[i+1][j+1] += cnt[i][j];
                else if(res[i][j] == '/') 
                    cnt[i+1][j-1] += cnt[i][j];
            }
        }
        int valid = 1;
        for(int i=1; i<=C; i++){
            if(res[R+1][i] != ori[i]){
                valid = 0;
            }
        }
        if(!valid){
            printf("IMPOSSIBLE\n");
            continue;
        }
        printf("%d\n", R+1);
        for(int i=1; i<=R; i++){
            for(int j=1; j<=C; j++) 
                printf("%c", res[i][j]);
            printf("\n");
        }
        for(int i=1; i<=C; i++) 
            printf(".");
        printf("\n");
    }
    return 0;
}