#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int cancelledorNot(int n,int k,vector<int>& a);
int main(){
    int t;
   
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        int k;
        cin >> n >> k;
        vector<int> a(n);
        for(int a_i = 0;a_i < n;a_i++){
           cin >> a[a_i];
        }
        cancelledorNot(n,k,a);
    }
     return 0;
}

int cancelledorNot(int n,int k,std::vector<int>& a)
    {
     int before=0,after=0;
for(int a_i = 0;a_i < n;a_i++)
        {
        if(a[a_i]>0)
            after++;
        else
            before++;
}
        if(before>=k)
           cout<<"NO"<<endl;
        else
            cout<<"YES"<<endl;
    
    return 0;
}
    
   
