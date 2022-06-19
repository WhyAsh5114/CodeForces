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
        string s;
        cin >> s;

        int ls = 0;
        for (int i = 0; i < 3; i++) {
            ls += (int)s[i];
        }

        int rs = 0;
        for (int i = 3; i < 6; i++) {
            rs += (int)s[i];
        }

        if (ls == rs) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}