#include <bits/stdc++.h>

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
        int x[n];
        for (int i = 0; i < n; i++)
            cin >> x[i];
        
        if (x[n-1] - x[0] - n + 1 <= 2)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}