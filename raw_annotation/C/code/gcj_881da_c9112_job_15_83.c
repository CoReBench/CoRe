#include <stdio.h>
int moves[50000];
char in_str[100000];
void job();
int main(){
  int t;
  scanf("%d", &t);
  for(int i=1; i<=t; i++){
    printf("Case #%d: ", i);
    job();
    printf("\n");
  }
  return 0;
}
void job(){
  char ggg = 'E' ^ 'S';
  int n;
  int goodp=-1;
  int movesp=0;
  char cur = 'E';
  scanf("%d%s", &n, in_str);
  n = n*2 - 2;
  moves[0]=0;
  for(int i=0; i<n; i++) {
    if(in_str[i] != cur){
      cur = cur ^ ggg;
      moves[movesp+1] = 1;
      movesp += 1;
    }
    else{
      moves[movesp]++;
      if( ((moves[0]) && (i%2)) || (!(moves[0]) && !(i%2)))
        goodp=movesp;
    }
  }
  int parity = movesp;
  if(moves[0] != 0)
    parity++;
  if(parity % 2 == 0){
    int En=0;
    for(int i=0; i<=movesp; i+=2)
      En+=moves[i];
    if(moves[0] == 0){
      for(int i=0; i<En; i++)
        printf("E");
      for(int i=0; i<n-En; i++)
        printf("S");
    }
    else{
      for(int i=0; i<n-En; i++)
        printf("S");
      for(int i=0; i<En; i++)
        printf("E");
    }
  }
  else{
    int s1=0,s2=0,e1=0,e2=0;
    for(int i=0; i<goodp; i+=2)
      e1+=moves[i];
    for(int i=1; i<goodp; i+=2)
      s1+=moves[i];
    for(int i= 2*((goodp+1)/2); i<=movesp; i+=2)
      e2+=moves[i];
    for(int i=2*(goodp/2)+1; i<=movesp; i+=2)
      s2+=moves[i];
    if(moves[0] == 0){
      for(int i=-1; i<e1; i++)
        printf("E");
      for(int i=0; i<s1+s2; i++)
        printf("S");
      for(int i=1; i<e2; i++)
        printf("E");
    }
    else{
      for(int i=-1; i<s1; i++)
        printf("S");
      for(int i=0; i<e1+e2; i++)
        printf("E");
      for(int i=1; i<s2; i++)
        printf("S");
    }
  }
}