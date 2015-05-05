#include<stdio.h>
int A[100],q,i,length;
int PARTITION(int A[],int p,int r){
	int x,i,j,tmp;
	x = A[r];
	i = p -1;
	for(j = p;j <= r-1;j++){
		if(A[j] <= x){
			i++;
			tmp = A[j];
			A[j] = A[i];
			A[i] = tmp;
		}
	}
	tmp = A[r];        //注意是A[r] 和 A[i+1] 的交换
	A[r] = A[i+1];
	A[i+1] = tmp;
	return i+1;
	
}
int QUICKSORT(int A[],int p,int r){
	if(p < r){
		q = PARTITION(A,p,r);
		QUICKSORT(A,p,q-1);  //注意 q-1
		QUICKSORT(A,q+1,r); //注意 q+1
	}
}

int main(){
	scanf("%d",&length);
	for(i=0;i<length;i++)
		scanf("%d",&A[i]);
	//q = PARTITION(A,0,length-1);
	//printf("%d \n",q);
	QUICKSORT(A,0,length-1);
	for(i = 0;i<length;i++)
		printf("%d,",A[i]);
	return 0;
}
