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
        int n;
        cin >> n;

        int a[n];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        bool odds_are_even = false;
        if (a[1] % 2 == 0) {
            odds_are_even = true;
        }
        bool odds_have_same_parity = true;
        for (int i = 3; i < n; i += 2) {
            if ((a[i] % 2 == 0) != odds_are_even) {
                odds_have_same_parity = false;
                break;
            }
        }
        if (!odds_have_same_parity) {
            cout << "NO" << endl;
            continue;
        }

        bool evens_are_even = false;
        if (a[0] % 2 == 0) {
            evens_are_even = true;
        }
        bool evens_have_same_parity = true;
        for (int i = 0; i < n; i += 2) {
            if ((a[i] % 2 == 0) != evens_are_even) {
                evens_have_same_parity = false;
                break;
            }
        }
        if (!evens_have_same_parity) {
            cout << "NO" << endl;
            continue;
        }

        cout << "YES" << endl;
    }
}