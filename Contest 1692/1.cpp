#include <bits/stdc++.h>
#define endl "\n"
typedef long long ll;
using namespace std;

void solve()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    int ans = 0;
    if (b > a) {
        ans += 1;
    }
    if (c > a) {
        ans += 1;
    }
    if (d > a) {
        ans += 1;
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