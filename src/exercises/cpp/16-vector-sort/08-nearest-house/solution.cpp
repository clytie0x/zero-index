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
        int p;
        cin >> p;
        int k = lower_bound(house.begin(), house.end(), p) - house.begin();
        int answer;
        if (k == n) {
            answer = house[n - 1];
        } else if (k == 0) {
            answer = house[0];
        } else if (p - house[k - 1] <= house[k] - p) {
            answer = house[k - 1];
        } else {
            answer = house[k];
        }
        cout << answer << '\n';
    }
    return 0;
}
