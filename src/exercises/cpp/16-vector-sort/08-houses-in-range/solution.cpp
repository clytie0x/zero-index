#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> house(n);
    for (int &x : house) {
        cin >> x;
    }
    sort(house.begin(), house.end());
    for (int i = 0; i < q; i++) {
        int left, right;
        cin >> left >> right;
        auto first = lower_bound(house.begin(), house.end(), left);
        auto past = upper_bound(house.begin(), house.end(), right);
        cout << past - first << '\n';
    }
    return 0;
}
