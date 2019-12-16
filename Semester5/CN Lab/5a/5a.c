#include<stdio.h>
#include<string.h>
#define N strlen(g) 

char t[28],cs[28],g[] = "10001000000100001";
int a,i,j,choice;

void xor(){
	for( i = 1; i < N; i++)
		cs[i] = ((cs[i] == g[i])?'0':'1'); 
}
void crc(){
	for(j = 0 ; j < N ; j++)
		cs[j] = t[j];
	do{
		if(cs[0]=='1')
			xor();
		for (i = 0; i < N-1; ++i)
			cs[i] = cs[i+1];
		cs[i] = t[j++];
	}while(j<=a+N-1);
}
int main(){
	printf("Enter the input data\n");
	scanf("%s",t);
	printf("Generated Polynomial is %s\n",g );
	a = strlen(t);
	for (int i = a ; i < a+N-1; i++)
		t[i] = '0';
	printf("Modified data is %s\n",t);
	crc();
	printf("Checksum value is %s\n",cs);
	for (int i = a; i < a+N-1; ++i)
	t[i] = cs[i-a];
	printf("The final codeword is %s\n",t );
	printf("Test error detection? 0(Yes) 1(No)?\n");
	scanf("%d",&choice);
	if(choice == 0){
		do{
			printf("Enter the position where you wanna insert the error\n");
			scanf("%d",&choice);
		}while(choice == 0 || choice>a+N-1);
		t[choice-1] = (t[choice-1]=='0');
		printf("\nErroneous data : %s\n",t);
	}
}