#include<stdio.h>
void alienpylon(int, int, int);
int main()
{
    int n,i;
    int r,c;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d %d",&r,&c);
        alienpylon(r,c,i);
    }
    return 0;
}
void alienpylon(int a,int b,int i)
{
    int k,temp1=a,temp2=b;
    if(b>=a)
    {
        if(b-a==1||a+1==b||a-1==b||b+1==a||b-1==a||a==b)
        {
            printf("Case #%d: IMPOSSIBLE\n",i+1);
        }
        else
        {
            printf("Case #%d: POSSIBLE\n",i+1);
            for(k=1;k<=a*b;k++)
            {
                temp1+=(((b/a)-1)%a);
                temp1=temp1%a;
                temp2+=(((b%a)+1)%b);
                temp2=temp2%b;
                printf("%d %d\n",temp1+1,temp2+1);
            }
        }
    }else{
        if(a-b==1||a+1==b||a-1==b||b+1==a||b-1==a||a==b)
        {
            printf("Case #%d: IMPOSSIBLE\n",i+1);
        }
        else
        {
            printf("Case #%d: POSSIBLE\n",i+1);
            for(k=1;k<=a*b;k++)
            {
                temp2+=(((a/b)-1)%b);
                temp2=temp2%b;
                temp1+=(((a%b)+1)%a);
                temp1=temp1%a;
                printf("%d %d\n",temp2+1,temp1+1);
            }
        }
    }
}