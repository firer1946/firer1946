#include<stdio.h>
int C[100],j,B[100],length;
int COUNTING_SORT(int A[],int B[],int k){
	int i;
	for(i=0;i<=k;i++)
		C[i] = 0;
	for(j=0;j< length;j++)
		C[A[j]] = C[A[j]] + 1;
	for(i=1;i<=k;i++)
		C[i] = C[i] + C[i-1];
	for(j=length -1 ;j >= 0 ;j--){
		B[C[A[j]]] = A[j];
		C[A[j]] = C[A[j]] - 1;
	}
	//for(i=0;i<=k;i++)
	//	printf("%d,",C[i]);
	printf("\n");
		
}
int main(){
	int A[100];
	scanf("%d",&length);
	printf("请输入100以内的数！！");
	for(j = 0;j<length;j++)
		scanf("%d",&A[j]);
	COUNTING_SORT(A,B,100);
	for(j = 1;j<=length;j++)
		printf("%d,",B[j]); //因为C[]中没有0，所以从1开始输出
	return 0;
}
