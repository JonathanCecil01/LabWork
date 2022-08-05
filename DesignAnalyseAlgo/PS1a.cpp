#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
    int arr[] = {1, 2, 3, 4, 5,6 ,7,8,12,3,3,2};
    int j = 11;
    int i=0;
    while(i<j)
    {
        if(arr[j]%2==0 && arr[i]%2!=0)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        j--;
        i++;
    }
    for(int i =0;i<12;i++)
    {
        cout<<arr[i]<<endl;
    }
}
