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
        int n, m;
        cin >> n >> m;

        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        sort(a.rbegin(), a.rend());
        long long int total = a[0] + 1;
        for (int i = 0; i < n-1; i++) {
            total += 1 + a[i];
            if (total > m) {
                cout << "NO" << endl;
                break;
            }
        }

        if (total <= m) {
            cout << "YES" << endl;
        }
    }
}