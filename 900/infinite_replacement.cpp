#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        string s, t;
        cin >> s >> t;

        long long int possibilities = 0;
        if (t == "a")
            possibilities = 1;
        else if (t.find("a") != t.npos)
            possibilities = -1;
        else
            possibilities = pow(2, s.length());
        
        cout << possibilities << endl;
    }
}