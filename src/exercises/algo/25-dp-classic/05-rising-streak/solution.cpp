#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> tails;
    for (int i = 0; i < n; i++) {
        int value;
        cin >> value;
        auto it = lower_bound(tails.begin(), tails.end(), value);
        if (it == tails.end()) {
            tails.push_back(value);
        } else {
            *it = value;
        }
    }
    cout << tails.size() << '\n';
    return 0;
}
