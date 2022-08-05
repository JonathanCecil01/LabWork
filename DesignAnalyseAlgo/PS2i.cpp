#include <iostream>

using namespace std;

int main()
{
    int arr[4][4] = {{3, 5, 7, 25}, {17, 20, 24, 36}, {21, 23, 27, 38}, {28, 29, 30, 40}};
    int arr2[8] = {0};
    int key = 31  ;
    int j=0;
    for(int i=0;i<4;i++)
    {
        if(key==arr[i][0] || key==arr[i][3])
        {
            cout<<"Key Found"<<endl;
            return 1;
        }
        if(key>arr[i][0] && key<arr[i][3])
        {
            arr2[j] = arr[i][1];
            j++;
            arr2[j] = arr[i][2];
            j++;
        }
    }
    int k =0;
    while(arr2[k]!=0)
    {
        if(arr2[k++]==key)
        {
            cout<<"KeyFound"<<endl;
            return 1;
        }
    }
    cout<<"KeyNotFound"<<endl;
}
