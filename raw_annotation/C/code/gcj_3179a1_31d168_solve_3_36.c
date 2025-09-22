#include<stdio.h>
#include<string.h>
void solve(int T)
{
  int MC[26] = {10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10};
  int O[26]= {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
  char out[10];
  int U;
  scanf("%d", &U);
  int i=0;
  char R[U], M[U];
  int lr, lm;
  while(i<10000)
  {
    scanf("%s %s", M, R); 
    lr=strlen(R);
    lm=strlen(M);
    O[R[lr-1]-'A'] = 1;
    if(lr==lm)
    {
      O[R[0]-'A'] = 1;
      if(MC[R[0]-'A'] > M[0]-'0')
      {
        MC[R[0]-'A']= M[0]-'0';
      } 
    }
    i++;
  }
  for(i=0; i<26; i++)
  {
    if(O[i])
      out[MC[i]%10]='A'+i;
  }
  printf("Case #%d: %s\n",T,out);
  return;
}
int main()
{
	int T,_T;
	scanf("%d", &T);
	_T=T;
	while(T--)
	{
		solve(_T-T);
	}
	return 0;
}