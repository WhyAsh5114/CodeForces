#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int c = n / 2020;
        if (c < n % 2020) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
        }
    }
}