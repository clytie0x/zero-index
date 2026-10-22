#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<long long> weight, load;

bool place(int i)
{
    if (i == n) {
        for (int b = 1; b < k; b++) {
            if (load[b] != load[0]) {
                return false;
            }
        }
        return true;
    }
    for (int b = 0; b < k; b++) {
        load[b] += weight[i];
        if (place(i + 1)) {
            return true;
        }
        load[b] -= weight[i];
    }
    return false;
}

int main()
{
    cin >> n >> k;
    weight.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> weight[i];
    }
    load.assign(k, 0);
    cout << (place(0) ? "YES" : "NO") << '\n';
    return 0;
}
