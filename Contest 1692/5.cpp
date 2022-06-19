#include <bits/stdc++.h>
#define endl "\n"
typedef long long ll;
using namespace std;

void solve()
{
    int n, s;
    cin >> n >> s;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += a[i];
    }
    int diff = total - s;

    if (s > total) {
        cout << -1 << endl;
        return;
    } else if (s == total) {
        cout << 0 << endl;
        return;
    }

    vector<int> lp = {0};
    for (int i = 0; i < n; i++) {
        if (a[i] == 1) {
            lp.push_back(i + 1);
        }
    }

    reverse(a, a+n);
    vector<int> rp = {0};
    for (int i = 0; i < n; i++) {
        if (a[i] == 1) {
            rp.push_back(i + 1);
        }
    }

    int ans = n;
    for (int i = 0; i <= diff; i++) {
        ans = min(lp[diff-i] + rp[i], ans);
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