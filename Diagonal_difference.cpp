#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    int sumLRD=0, sumRLD=0;
    int sumABS=0;
    cin >> n;
    vector< vector<int> > a(n,vector<int>(n));
    for(int a_i = 0;a_i < n;a_i++){
       for(int a_j = 0;a_j < n;a_j++){
          cin >> a[a_i][a_j];
       }
    }
    for(int a_i = 0;a_i < n;a_i++){
       for(int a_j = 0;a_j < n;a_j++)
           {
           if(a_j==a_i)
               sumLRD+=a[a_i][a_j];
       }
    }
    for(int a_i = 0;a_i < n;a_i++){
       for(int a_j = 0;a_j < n;a_j++)
           {
           if(a_j==(n-a_i-1))
               sumRLD+=a[a_i][a_j];
       }
    }
    sumABS=abs(sumLRD-sumRLD);
    cout<<sumABS;
    
    return 0;
}
