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
        int x, y;
        cin >> x >> y;

        if (y % x != 0) {
            cout << "0 0" << endl;
            continue;
        }

        cout << "1 " << y / x << endl;
    }
}