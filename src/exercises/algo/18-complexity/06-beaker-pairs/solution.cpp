#include <bits/stdc++.h>
using namespace std;

#define MAX_VOLUME 1000000
long long how_many[MAX_VOLUME + 1];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        how_many[v]++;
    }
    long long ways = 0;
    for (int d = 1; d <= MAX_VOLUME; d++) {
        if (how_many[d] == 0) {
            continue;
        }
        ways += how_many[d] * (how_many[d] - 1);
        for (int m = 2 * d; m <= MAX_VOLUME; m += d) {
            ways += how_many[d] * how_many[m];
        }
    }
    cout << ways << '\n';
    return 0;
}
