#include <bits/stdc++.h>
#define endl "\n"
typedef long long ll;

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

        int min = *min_element(a, a+n);
        ll ans = 0;
        for (int i = 0; i < n; i++) {
            ans += a[i] - min;
        }

        cout << ans << endl;
    }
}