#include<stdio.h>
int main(){
	int i,j,a[5],tmp;
	for(i=0;i<5;i++){
		scanf("%d",&a[i]);
	}
	for(i=0;i<=4;i++){
		for(j=4;j>=i+1;j--){
			if(a[j] < a[j-1]){	
				tmp = a[j-1];
				a[j-1] = a[j];
				a[j] = tmp;
			}
		}
	}
	for(i=0;i<5;i++)
		printf("%d.",a[i]);
	return 0;
}
