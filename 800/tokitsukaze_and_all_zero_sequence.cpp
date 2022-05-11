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
        int a[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        sort(a, a+n);

        int z = 0;
        for (int n : a)
            if (n == 0)
                z++;
        
        if (z > 0) {
            cout << n-z << endl;
        } else {
            bool dup = false;
            for (int i = 0; i < n-1; i++) {
                if (a[i] == a[i+1]) {
                    dup = true;
                    cout << n << endl;
                    break;
                }
            }
            if (!dup)
                cout << n+1 << endl;
        }
    }
}