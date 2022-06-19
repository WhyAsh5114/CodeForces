#include <bits/stdc++.h>
#define endl "\n"
typedef long long ll;
using namespace std;

void solve()
{
    int n, m;
    cin >> n >> m;

    int a[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int sum = 0;

            int tx = i, ty = j;
            while (tx < n && ty < m) {
                sum += a[tx][ty];
                tx++; ty++;
            }

            tx = i, ty = j;
            while (tx < n && ty >= 0) {
                sum += a[tx][ty];
                tx++; ty--;
            }

            tx = i, ty = j;
            while (tx >= 0 && ty < m) {
                sum += a[tx][ty];
                tx--; ty++;
            }

            tx = i, ty = j;
            while (tx >= 0 && ty >= 0) {
                sum += a[tx][ty];
                tx--; ty--;
            }
            
            sum -= a[i][j] * 3;
            ans = max(ans, sum);
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