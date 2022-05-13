#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    vector<string> answers;
    while (t--) {
        int a, b, c, x, y;
        cin >> a >> b >> c >> x >> y;

        x -= min(a, x);
        y -= min(b, y);
        
        if (x + y <= c)
            answers.push_back("YES");
        else
            answers.push_back("NO");
    }

    for (string s : answers)
        cout << s << endl;
}