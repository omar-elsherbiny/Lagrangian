#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")
#pragma GCC optimize("-Ofast")
#include <bits/stdc++.h>

using namespace std;

typedef int in;
#define int long long
#define s second
#define f first
const long double EPS=1e-9;
const int MOD=1e9+7;
const int N=1e6;

in main(){
    int t;
    cin >> t;

    int n=t;
    pair<double,double> pnts[n];
    double k[n];
    while(t --){
        cin >> pnts[t].f >> pnts[t].s;
    }
    for (int i=0;i<n;i++) {
        double prod=1;
        for(int j=0;j<n;j++) {
            if (j==i) {continue;}
            prod*=(pnts[i].f-pnts[j].f);
        }
        k[i]=pnts[i].s * 1/prod;
        cout << k[i] << "\n";
    }
    return 0;
}