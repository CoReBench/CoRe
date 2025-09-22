#include <stdio.h>
void judge(int x){
	if(x == 1){
		printf("Yes\n");
	}else if(x == 0){
		printf("No\n");
	} 
}
int main(void) {
	char word[100];
	scanf("%s",&word);
	int i=0;
	int flagC=0;
	int flagF=0;
	int SuccessFlag=0;
	while(word[i]!='\0'){
		if(word[i]=='C'){
			flagC = i;
			SuccessFlag++;
		}else if(word[i]=='F'){
			flagF = i;
		}
		i++;
	}
	if(SuccessFlag>1 && flagC < flagF){
		judge(1);
	}else{
		judge(0);
	}
	return 0;
}