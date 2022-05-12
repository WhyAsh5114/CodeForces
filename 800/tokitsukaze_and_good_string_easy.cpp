#include <bits/stdc++.h>

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
        string s;
        cin >> s;
        int a[n];
        for (int i = 0; i < n; i++)
            a[i] = s[i];
        
        int ans = 0;
        int c = 1;
        for (int i = 1; i < n; i++) {
            if (a[i] == a[i-1]) {
                c++;
            } else {
                if (c % 2 != 0) {
                    ans++;
                    a[i] = a[i-1];
                    c = 0;
                } else {
                    c = 1;
                }
            }            
        }

        cout << ans << endl;
    }
}