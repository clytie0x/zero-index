#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<int> value(n);
    for (int i = 0; i < n; i++) {
        cin >> value[i];
    }
    for (int start = 0; start + k <= n; start++) {
        int highest = value[start];
        int lowest = value[start];
        for (int j = start + 1; j < start + k; j++) {
            highest = max(highest, value[j]);
            lowest = min(lowest, value[j]);
        }
        long long swing = (long long)highest - lowest;
        cout << swing << (start + k < n ? ' ' : '\n');
    }
    return 0;
}
