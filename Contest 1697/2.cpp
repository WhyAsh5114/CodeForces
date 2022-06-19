#include <bits/stdc++.h>
#define endl "\n"

typedef long long ll;

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, q;
    cin >> n >> q;
    ll p[n];
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }

    sort(p, p+n, greater<int>());
    for (int i = 1; i < n; i++) {
        p[i] += p[i-1];
    }

    for (int i = 0; i < q; i++) {
        int x, y;
        cin >> x >> y;

        if (x != y) {
            cout << p[x-1] - p[x-y-1] << endl;
        } else {
            cout << p[x-1] << endl;
        }
    }
}