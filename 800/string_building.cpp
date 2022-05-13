#include <bits/stdc++.h>

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
        
        int n = s.size();
        bool ans = true;
        for (int i = 0; i < n; i++) {
            if ((i == 0 || s[i] != s[i - 1]) && (i == n - 1 || s[i] != s[i + 1])) {
                ans = false;
            }
        }

        if (ans)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}