#include <stdio.h>
#include <stdlib.h>
#pragma GCC optimize ("O3")
inline static int gl(void){
    int x = 0;
    for(;;){
        unsigned int c = getchar_unlocked() - 48;
        if(c < 10){
            x = x*10 + c;
        }else{
            break;
        }
    }
    return x;
}
inline static void pl(unsigned int s){
    char str[9];
    int pos=9;
    if(s==0){
        putchar_unlocked('0');
        return;
    }
    do{
        pos--;
        str[pos]=s%10+48;
        s/=10;
    }while(s!=0);
    for(; pos<9; pos++){
        putchar_unlocked(str[pos]);
    }
}
int main(void){
    static unsigned short out[1000000];
    char a[501];
    const int h=gl(), w=gl();
    int pos=0;
    char haveCoin = 0;
    short old_y, old_x;
    for(int i=1; i<=h; i++){
        for(int j=1; j<=w; j++){
            int t = getchar_unlocked() - 48;
            getchar_unlocked();
            a[j] = t;
        }
        if(i%2==1){
            for(int j=1; j<=w; j++){
                if(haveCoin){
                    out[4*pos+0]=old_y;
                    out[4*pos+1]=old_x;
                    out[4*pos+2]=i;
                    out[4*pos+3]=j;
                    pos++;
                }
                haveCoin ^= a[j]&1;
                old_y = i;
                old_x = j;
            }
        }else{
            for(int j=w; j>0; j--){
                if(haveCoin){
                    out[4*pos+0]=old_y;
                    out[4*pos+1]=old_x;
                    out[4*pos+2]=i;
                    out[4*pos+3]=j;
                    pos++;
                }
                haveCoin ^= a[j]&1;
                old_y = i;
                old_x = j;
            }
        }
    }
    pl(pos); putchar_unlocked('\n');
    for(int i=0; i<pos; i++){
        pl(out[4*i+0]); putchar_unlocked(' ');
        pl(out[4*i+1]); putchar_unlocked(' ');
        pl(out[4*i+2]); putchar_unlocked(' ');
        pl(out[4*i+3]); putchar_unlocked('\n');
    }
    return 0;
}