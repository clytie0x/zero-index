#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long limit;
    cin >> n >> limit;
    vector<long long> weight(n);
    for (int i = 0; i < n; i++) {
        cin >> weight[i];
    }
    sort(weight.begin(), weight.end());
    int light = 0, heavy = n - 1, boats = 0;
    while (light <= heavy) {
        if (light < heavy && weight[light] + weight[heavy] <= limit) {
            light++;
        }
        heavy--;
        boats++;
    }
    cout << boats << '\n';
    return 0;
}
