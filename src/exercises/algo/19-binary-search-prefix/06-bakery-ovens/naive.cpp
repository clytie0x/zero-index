#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long trays;
    cin >> n >> trays;
    vector<long long> minutes(n);
    for (int i = 0; i < n; i++) {
        cin >> minutes[i];
    }
    long long time = 0;
    while (true) {
        time++;
        long long baked = 0;
        for (int i = 0; i < n; i++) {
            baked += time / minutes[i];
        }
        if (baked >= trays) {
            break;
        }
    }
    cout << time << '\n';
    return 0;
}
