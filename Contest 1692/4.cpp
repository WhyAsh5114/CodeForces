#include <bits/stdc++.h>
#define endl "\n"
typedef long long ll;
using namespace std;

void solve()
{
    string s;
    int x;
    cin >> s >> x;

    int h = (s[0] - '0') * 10 + (s[1] - '0');
    int m = (s[3] - '0') * 10 + (s[4] - '0');
    int ih = h, im = m;
    int ha = x / 60;
    int ma = x % 60;

    bool started = false;
    set<pair<string, string>> palindromes;
    while (!(ih == h && im == m) || !started) {
        string sh = to_string(h);
        string sm = to_string(m);

        if (sh.length() == 1)
            sh = "0" + sh;
        if (sm.length() == 1)
            sm = "0" + sm;

        string r_sm = sm;
        reverse(r_sm.begin(), r_sm.end());
        if (sh == r_sm) {
            palindromes.insert({sh, sm});
        }

        h += ha, m += ma;
        if (h > 23) {
            h %= 24;
        }
        if (m > 59) {
            h += 1;
            m %= 60;
            if (h == 24) {
                h = 0;
            }
        }
        started = true;
    }

    cout << palindromes.size() << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}