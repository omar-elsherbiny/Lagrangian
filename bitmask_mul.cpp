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

int nig[105];

in main(){
    int t;
    cin >> t;

    int n=t;
    int k[n];

    for (int i=0;i<n;i++) {
        cin >> k[i];
    }
    for (int i=0;i<(1<<n);i++) {
        int p=0,c=1;
        for (int j=0;j<n;j++) {
            if (i&(1<<j)) {
                p++;
            } else {
                c*=k[j];
            }
        }
        nig[p]+=c;
    }
    for (int i=0;i<n+1;i++) {
        cout << nig[i] << "x" << i << "+";
    }
    return 0;
}