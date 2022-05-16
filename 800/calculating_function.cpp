#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long int n;
    cin >> n;
    if (n % 2 == 0) {
        cout << n / 2 << endl;
    } else {
        cout << -(n+1) / 2 << endl;
    }
}