#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int minswaps(char* p, int d, int len);
int main()
{
	int n,i;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		int d;
		char p[31];
		scanf("%d ",&d);
		scanf("%s",p);
		int r=minswaps(p,d,strlen(p));
		if(r==-1)
			printf("Case #%d: IMPOSSIBLE\n",i+1 );
		else
			printf("Case #%d: %d\n",i+1,r );
	}
}
int minswaps(char* p, int d, int len)
{
    if(len==2)
    {
        if(p[0]=='S' && p[1]=='C')
            return(0);
        if(p[0]=='S'&&p[1]=='S')
        {
            if(d<2)
                return(-1);
            else
                return(0);
        }
        if(p[0]=='C' && p[1]=='S')
        {
            if(d<2)
                return(1);
            else
                return(0);
        }
        return(0);
    }
    int i,strength=1,damage=0,temp,k=0,swaps=0,flag=0;
    int * a=(int*)malloc(sizeof(int)*len);
    for(i=0;i<len;i++)
    {
        if(p[i]=='S')
        {
            damage+=strength;
            a[k++]=strength;
        }
        else
        {
            strength*=2;
            a[k++]=strength;
        }
    }
    if(damage<=d)
        return(0);
    i=len-1;
    while(!flag)
    {
          flag=1;
          i=len-1;
          while(damage-d>0 && i>0)
          {
              while(p[i]!='S')
                  i--;
              if(p[i-1]=='S')
                  i--;
              else
              {
                  flag=0;
                  p[i]='C';
                  p[i-1]='S';
                  damage-=a[i];
                  if(i-1==0)
                  {
                      a[i-1]=1;
                      a[i]=2;
                  }
                  else
                  {
                    a[i-1]=a[i-2];
                    a[i]=2*a[i-1];
                  }
                  damage+=a[i-1];
                  swaps++;
              }
              if(i==1 && p[i-1]=='S')
              {
                break;
              }
          }
    }
    free(a);
    if(damage-d<=0)
        return(swaps);
    else
        return(-1);
}