#include <bits/stdc++.h>
#define endl "\n"
typedef long long ll;
using namespace std;

void solve()
{
    int n;
    cin >> n;
    map<int, int> m;
    for (int i = 0; i < n; i++) {
        int e;
        cin >> e;
        m[e] += 1;
    }

    int ans = 0, evens = 0;
    for (auto p : m) {
        if (p.second % 2 != 0) {
            ans++;
        } else {
            evens += 1;
        }
    }
    ans += evens - (evens % 2);
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