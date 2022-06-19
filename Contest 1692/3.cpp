#include <bits/stdc++.h>
#define endl "\n"
typedef long long ll;
using namespace std;

void solve()
{
    string board[8];
    for (int i = 0; i < 8; i++) {
        cin >> board[i];
    }

    bool active = false;
    for (int i = 0; i < 8; i++) {
        int atk = 0, ind = 0;
        for (int j = 0; j < 8; j++) {
            if (board[i][j] == '#') {
                atk++;
                ind = j;
            }
        }
        if (atk == 2 && !active) {
            active = true;
        } else if (atk == 1 && active) {
            cout << i + 1 << " " << ind + 1 << endl;
            break;
        }
    }
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