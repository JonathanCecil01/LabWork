#include <iostream>
using namespace std;

int binarySearch(int arr[], int key, int n)
{
    int left = 0;
    int right = n-1;
    int index=-1;
    int mid =0;
    while(left<=right)
    {
        mid = (left+right)/2;
        if(arr[mid]>key)
        {
            right = mid-1;
        }
        else if(arr[mid]<key)
        {
            left= mid+1;
        }
    }
    return mid-1;
}


int main()
{
    int m = 7;
    int n = 5;
    int max = m>n?m:n;
    int A[7] = {2, 5, 8, 9, 12, 16, 20};
    int B[5] = {1, 4, 6, 11, 24};
    int pos = 6;
    int temp_pos = -1;
    int start = pos;
    int key =-1;
    if(pos<max)
    {
        if(max==m)
        {
            key = A[pos];
        }else{
            key = B[pos];
        }
    }else{
        if(max==m){
            key = A[m-1];
        }else{
            key = B[n-1];
        }
    }
    int index = binarySearch(A, key, m);
    int x=-1;
    while(1)
    {
        if(index==0){
            cout<<key<<endl;
            break;
        }
        else{
            if(index<start)
            {
                start = start/2;
                key = A[start];
                index = binarySearch(A, key, m);
                temp_pos = index+start;
            }
            else{
                start = n/2;
                key = B[start];
                index = binarySearch(B, key, n);
                temp_pos = index+start;
            }
        }
        cout<<temp_pos<<endl;
    }




int main()
{
    int m = 7;
    int n = 5;
    int max = m>n?m:n;
    int A[7] = {2, 5, 8, 9, 12, 16, 20};
    int B[5] = {1, 4, 6, 11, 24};
    int pos = 6;

}

















}
