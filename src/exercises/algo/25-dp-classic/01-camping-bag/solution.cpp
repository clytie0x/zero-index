#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, capacity;
    cin >> n >> capacity;
    vector<long long> best(capacity + 1, 0);
    for (int i = 0; i < n; i++) {
        int weight;
        long long value;
        cin >> weight >> value;
        for (int c = capacity; c >= weight; c--) {
            best[c] = max(best[c], best[c - weight] + value);
        }
    }
    cout << best[capacity] << '\n';
    return 0;
}
