#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<long long> need(n + 1), got(n + 1, 0);
    int thirsty = 0;
    for (int tree = 1; tree <= n; tree++) {
        cin >> need[tree];
        if (need[tree] > 0) {
            thirsty++;
        }
    }
    int answer = (thirsty == 0 ? 0 : -1);
    for (int j = 1; j <= q; j++) {
        int l, r, w;
        cin >> l >> r >> w;
        if (answer != -1) {
            continue;
        }
        for (int tree = l; tree <= r; tree++) {
            bool was_thirsty = got[tree] < need[tree];
            got[tree] += w;
            if (was_thirsty && got[tree] >= need[tree]) {
                thirsty--;
            }
        }
        if (thirsty == 0) {
            answer = j;
        }
    }
    cout << answer << '\n';
    return 0;
}
