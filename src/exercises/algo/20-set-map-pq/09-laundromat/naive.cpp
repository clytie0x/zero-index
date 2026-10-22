#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<long long> finish(k + 1, 0);
    for (int i = 0; i < n; i++) {
        long long arrive, duration;
        cin >> arrive >> duration;
        long long earliest = finish[1];
        for (int id = 2; id <= k; id++) {
            earliest = min(earliest, finish[id]);
        }
        long long start = max(arrive, earliest);
        int machine = 1;
        while (finish[machine] > start) {
            machine++;
        }
        finish[machine] = start + duration;
        cout << machine << ' ' << finish[machine] << '\n';
    }
    return 0;
}
