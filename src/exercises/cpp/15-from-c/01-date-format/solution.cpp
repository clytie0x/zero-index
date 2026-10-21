#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string date;
        cin >> date;
        cout << date.substr(6, 4) << '-' << date.substr(3, 2) << '-' << date.substr(0, 2) << '\n';
    }
    return 0;
}
