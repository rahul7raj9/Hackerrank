#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    float countpos=0.0, countneg=0.0, countzero=0.0;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }
    for(int arr_i = 0;arr_i < n;arr_i++)
        {
        if(arr[arr_i]>0)
            countpos++;
        else if(arr[arr_i]<0)
            countneg++;
            else
            countzero++;
    }
    cout<<countpos/n<<endl;
    cout<<countneg/n<<endl;
    cout<<countzero/n<<endl;
    
    return 0;
}
