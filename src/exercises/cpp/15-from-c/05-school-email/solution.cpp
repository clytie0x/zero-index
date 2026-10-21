#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string domain;
    int n;
    cin >> domain >> n;
    int valid = 0;
    for (int i = 0; i < n; i++) {
        string email;
        cin >> email;
        size_t at = email.find('@');
        if (at == string::npos || at == 0) {
            continue;
        }
        if (email.find('@', at + 1) != string::npos) {
            continue;
        }
        if (email.substr(at + 1) == domain) {
            cout << email.substr(0, at) << '\n';
            valid++;
        }
    }
    cout << valid << '\n';
    return 0;
}
