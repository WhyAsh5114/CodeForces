#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    int answers[t];
    for (int i = 0; i < t; i++) {
        int x, y, a, b;
        cin >> x >> y >> a >> b;

        if ((y - x) % (b + a) == 0) {
            answers[i] = (y - x) / (b + a);
        } else {
            answers[i] = -1;
        }
    }

    for (int i = 0; i < t; i++) {
        cout << answers[i] << endl;
    }
}