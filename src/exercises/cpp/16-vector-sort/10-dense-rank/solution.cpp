#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> points(n);
    for (int &p : points) {
        cin >> p;
    }
    vector<int> distinct = points;
    sort(distinct.begin(), distinct.end());
    distinct.erase(unique(distinct.begin(), distinct.end()), distinct.end());
    int d = distinct.size();
    for (int i = 0; i < n; i++) {
        int pos = lower_bound(distinct.begin(), distinct.end(), points[i]) - distinct.begin();
        if (i > 0) {
            cout << ' ';
        }
        cout << d - pos;
    }
    cout << '\n';
    return 0;
}
