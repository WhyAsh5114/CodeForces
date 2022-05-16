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
        long long int n;
        cin >> n;
        long long int min = 0;
        long long int max = 0;

        if (n % 2 != 0 || n < 4) {
            cout << -1 << endl;
            continue;
        }

        long long int ln = n;
        while (ln % 4 != 0) {
            max += 1;
            ln -= 6;
        }
        max += ln / 4;

        long long int sn = n;
        while (sn % 6 != 0)
        {
            min += 1;
            sn -= 4;
        }
        min += sn / 6;
        
        cout << min << " " << max << endl;
    }
}