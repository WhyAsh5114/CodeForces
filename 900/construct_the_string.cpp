#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n, a, b;
        cin >> n >> a >> b;

        int tb = 0;
        string s;
        for (int j = 0; j < n; j++)
        {
            if (tb >= b)
                tb = 0;
            s += char(97 + tb);
            tb += 1;
        }

        cout << s << endl;
    }
}