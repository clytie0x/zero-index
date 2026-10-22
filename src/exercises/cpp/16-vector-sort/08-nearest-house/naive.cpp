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
    for (int i = 0; i < q; i++) {
        int p;
        cin >> p;
        int answer = house[0];
        long long best = abs((long long)house[0] - p);
        for (int x : house) {
            long long gap = abs((long long)x - p);
            if (gap < best || (gap == best && x < answer)) {
                best = gap;
                answer = x;
            }
        }
        cout << answer << '\n';
    }
    return 0;
}
