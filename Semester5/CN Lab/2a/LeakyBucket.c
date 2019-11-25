#include<stdio.h>
#include<stdlib.h>
#define MIN(x,y) (x>y)?y:x

int main()
{
int orate=2,drop=0,cap=5,x,count=0,inp[10]={0},nsec,ch,i=0;
for(i=0;i<5;i++)
	inp[i]=rand()%10;
nsec=i;
printf("\nsecond\trecieved\tsent\tdropped\tremained\n");
for(i=0;count || i<nsec;i++)
{
 printf("%d\t",i+1);
 printf("%d\t\t",inp[i]);
 printf("%d\t ",MIN((inp[i]+count),orate));
 if((x=inp[i]+count-orate)>0)
 {
  if(x>cap)
  {
   count=cap;
   drop=x-cap;
  }
  else
  {
   count=x;
   drop=0;
  }
 }
 else
 {
  drop=0;
  count=0;
  }
 printf("%d\t%d \n",drop,count);
 }   // end of for loop
 return 0;
}