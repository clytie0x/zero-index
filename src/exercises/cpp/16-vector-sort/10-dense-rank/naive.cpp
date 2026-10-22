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
    vector<int> distinct;
    for (int p : points) {
        bool seen = false;
        for (int q : distinct) {
            if (q == p) {
                seen = true;
                break;
            }
        }
        if (!seen) {
            distinct.push_back(p);
        }
    }
    for (int i = 0; i < n; i++) {
        int rank = 1;
        for (int q : distinct) {
            if (q > points[i]) {
                rank++;
            }
        }
        if (i > 0) {
            cout << ' ';
        }
        cout << rank;
    }
    cout << '\n';
    return 0;
}
