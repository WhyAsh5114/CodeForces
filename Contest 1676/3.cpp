#include <bits/stdc++.h>
#define endl "\n"
typedef long long ll;

using namespace std;

void solve()
{
    int n, m;
    cin >> n >> m;
    string a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int ans = INT_MAX;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                continue;
            }
            int diff = 0;
            for (int k = 0; k < m; k++) {
                if (a[i][k] == 'a') {
                    diff += a[j][k] - 'a';
                } else if (a[i][k] == 'z') {
                    diff += 'z' - a[j][k];
                } else {
                    diff += min(abs(a[j][k] - a[i][k]), abs(a[i][k] - a[j][k]));
                }
            }
            ans = min(diff, ans);
        }
    }

    cout << ans << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}