#include <bits/stdc++.h>
#define endl "\n"
typedef long long ll;
using namespace std;

void solve()
{
    int n, q;
    cin >> n >> q;

    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a, a+n, greater<int>());

    for(int i = 1; i < n; i++) {
        a[i] += a[i-1];
    }

    while (q--) {
        int x;
        cin >> x;

        int *ans = lower_bound(a, a+n, x);
        if (ans == a+n) {
            cout << -1 << endl;
        } else {
            cout << ((ans - a) + 1) << endl;
        }
    }
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