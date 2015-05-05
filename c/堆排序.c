#include<stdio.h>
int A[11] = {0,42,25,9,10,23,32,2,15,34,54},length=10,largest,heap_size,i,tmp;
int MAX_HEAPIFY(int A[],int a){
	int l,r; // l <= 左儿子     r <= 右儿子
	l=2*a;
	r=2*a+1;
	//printf("%d \n",A[l]);
	
	if(l <= heap_size && A[l] > A[a])
		largest = l;
	else largest = a;
	if(r <= heap_size && A[r] > A[largest])
		largest = r;
 	if(largest != a){
		tmp = A[a];
		A[a] = A[largest];
		A[largest] = tmp;
		MAX_HEAPIFY(A,largest); //保持堆底下的性质
		
	}
	

}

int BUILD_MAX_HEAPIFY(int A[]){
	heap_size = length;
	for( i=length/2;i>=1;i--)
		MAX_HEAPIFY(A,i);

}
int main(){
	//printf("%d",A[9]);
	//MAX_HEAPIFY(A,5);
	BUILD_MAX_HEAPIFY(A);
	for(i = length;i >=2;i--){
		int tmp = A[i];
		A[i] = A[1];
		A[1] = tmp;
		heap_size = heap_size - 1; //减小堆长度
		MAX_HEAPIFY(A,1);
	 }
	for(i=1;i<11;i++)	
		printf("%d,",A[i]);
	return 0;
}
