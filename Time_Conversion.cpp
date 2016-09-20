#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <time.h>
#include <iomanip>
using namespace std;

int main(){
    string time;
    cin >> time;
    string hour = time.substr (0,2);
    string mins = time.substr (3,5);
    string secs = time.substr (6,8);
    string str = time.substr(8,10);

       int hrs = atoi(hour.c_str());
       int minuts = atoi(mins.c_str());
       int secons = atoi(secs.c_str());
   

            if(str=="AM")//(str.compare("AM") ))
            {
                if( hrs == 12){
                    hrs=0;}
            }
            else{
                     if( hrs == 12){
                         hrs=12;}
                    else{
                        hrs =(hrs+12) % 24;
                    }
               }
        
        cout <<setfill('0')<< setw(2)<<hrs<<":";
        cout<<setfill('0') << setw(2) <<minuts<<":";
        cout<<setfill('0') << setw(2) <<secons;

    return 0;
}
