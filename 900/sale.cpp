#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];
    
    sort(a, a+n);
    int money = 0;
    for (int i = 0; i < m; i++) {
        if (a[i] < 0) {
            money += -(a[i]);
        } else {
            break;
        }
    }
    
    cout << money << endl;
}