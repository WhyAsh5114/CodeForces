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

        sort(a, a+n);
        int counter = 1;
        int answer = -1;
        for (int i = 0; i < n-1; i++) {
            if (a[i] == a[i+1]) {
                counter++;
            } else {
                counter = 1;
            }
            if (counter >= 3) {
                answer = a[i];
                break;
            }
        }

        cout << answer << endl;
    }
}