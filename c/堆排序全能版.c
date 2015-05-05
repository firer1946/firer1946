#include<stdio.h>
int i,length,tmp,largest,heap_size,A[100];
int MAX_HEAPIFY(int A[],int a){
	int r,l;
	l = 2*a;
	r = 2*a + 1;
	if(l <= heap_size && A[l] > A[a])
		largest = l;
	else largest = a;
	if(r <= heap_size && A[r] > A[largest])
		largest = r;
	if(a != largest){
		tmp = A[largest];
		A[largest] = A[a];
		A[a] = tmp;
		MAX_HEAPIFY(A,largest);
	}
}
int BUILD_MAX_HEAPIFY(int A[]){
	heap_size = length;
	for( i = length/2;i>=1;i--)
		MAX_HEAPIFY(A,i);

} 

int main(){
	scanf("%d",&length);
	for(i=1;i<=length;i++)
		scanf("%d",&A[i]);
	BUILD_MAX_HEAPIFY(A);
	for(i=length;i>=2;i--){
		tmp = A[1];
		A[1] = A[i];
		A[i] = tmp;
		heap_size--;
		MAX_HEAPIFY(A,1);

	}
	for(i = 1;i <= length;i++)
		printf("%d,",A[i]);
	
	return 0;
}
