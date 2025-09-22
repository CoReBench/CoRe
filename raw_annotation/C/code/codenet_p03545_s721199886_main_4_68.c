#include <stdio.h>
int sum(int a,int b);
int sub(int a,int b);
int main(void){
	int i,n,a,b,c,d,x,op1,op2,op3,cnt=0;
	char op[2]={'+','-'};
	scanf("%d",&n);
	a=(n/1000)%10;
	b=(n/100)%10;
	c=(n/10)%10;
	d=n%10;
	for(;;){
		x=0;
		op1=0;
		op2=0;
		op3=0;
		for(i=0;i<3;i++){
			if((cnt<3)||(cnt==4)){
				x=sum(a,b);
				if(cnt<2){
					x=sum(x,c);
					if(cnt==0){
						x=sum(x,d);
					}else{
						x=sub(x,d);
						op3=1;
					}
				}else{
					x=sub(x,c);
					op2=1;
					if(cnt==2){
						x=sum(x,d);
					}else{
						x=sub(x,d);
						op3=1;
					}
				}
			}else{
				x=sub(a,b);
				op1=1;
				if((cnt==3)||(cnt==6)){
					x=sum(x,c);
					if(cnt==3){
						x=sum(x,d);
					}else{
						x=sub(x,d);
						op3=1;
					}
				}else{
					x=sub(x,c);
					op2=1;
					if(cnt==5){
						x=sum(x,d);
					}else{
						x=sub(x,d);
						op3=1;
					}
				}
			}
		}
		if(x==7){
			break;
		}
		cnt++;
	}
	printf("%d%c%d%c%d%c%d=7",a,op[op1],b,op[op2],c,op[op3],d);
	return 0;
}
int sum(int a,int b){
	return a+b;
}
int sub(int a,int b){
	return a-b;
}