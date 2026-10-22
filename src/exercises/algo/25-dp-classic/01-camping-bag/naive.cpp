#include <bits/stdc++.h>
using namespace std;

int n, capacity;
vector<int> weight;
vector<long long> value;
long long best_value = 0;

void try_items(int i, long long used, long long total)
{
    if (i == n) {
        best_value = max(best_value, total);
        return;
    }
    try_items(i + 1, used, total);
    if (used + weight[i] <= capacity) {
        try_items(i + 1, used + weight[i], total + value[i]);
    }
}

int main()
{
    cin >> n >> capacity;
    weight.resize(n);
    value.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> weight[i] >> value[i];
    }
    try_items(0, 0, 0);
    cout << best_value << '\n';
    return 0;
}
