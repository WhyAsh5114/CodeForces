#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a, b, c;
    cin >> a >> b >> c;
    int ans = (a+b) * c;
    ans = max(ans, a * (b+c));

    ans = max(ans, a+b+c);
    ans = max(ans, a*b*c);

    ans = max(ans, a+b*c);
    ans = max(ans, a*b+c);

    cout << ans << endl;
}