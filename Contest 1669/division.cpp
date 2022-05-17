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
        int rating;
        cin >> rating;

        if (rating <= 1399) {
            cout << "Division 4" << endl;
        } else if (rating <= 1599) {
            cout << "Division 3" << endl;
        } else if (rating <= 1899) {
            cout << "Division 2" << endl;
        } else {
            cout << "Division 1" << endl;
        }
    }
}