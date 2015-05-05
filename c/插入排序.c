#include<stdio.h>
int main(){
	int i,j,a[5],k,key;
	for(i=0;i<5;i++){
		scanf("%d",&a[i]);

	}
	for(i=1;i<5;i++){
		key=a[i];
		for(j=0;j<i;j++){
			if(a[j] > key){
				for(k=i;k>j;k--){     //这一步是关键，进行值的调换
					a[k] = a[k-1];
				}	
				a[j] = key;
				break;
			}

		}
	}
	for(i=0;i<5;i++)
		printf("%d.",a[i]);
	return 0;
}
