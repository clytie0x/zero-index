#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    set<string> guests;
    for (int i = 0; i < n; i++) {
        string name;
        cin >> name;
        guests.insert(name);
    }
    cout << guests.size() << '\n';
    for (const string &name : guests) {
        cout << name << '\n';
    }
    return 0;
}
