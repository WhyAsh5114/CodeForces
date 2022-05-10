#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{
        int t;
        cin >> t;
 
        int a[t];
        for (int i = 0; i < t; i++)
                cin >> a[i];
 
        for (int i = 0; i < t; i++) {
                int n = a[i];
                vector<int> k;
                int d = 0;
                while (n > 0) {
                        int digit = n % 10;
                        if (digit != 0)
                                k.push_back(digit * pow(10, d));
                        d++;
                        n /= 10;
                }
                cout << k.size() << endl;
                for (int n : k)
                        cout << n << " ";
                cout << endl;
        }