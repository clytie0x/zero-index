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
    deque<int> high, low;
    for (int i = 0; i < n; i++) {
        while (!high.empty() && value[high.back()] <= value[i]) {
            high.pop_back();
        }
        high.push_back(i);
        while (!low.empty() && value[low.back()] >= value[i]) {
            low.pop_back();
        }
        low.push_back(i);
        if (high.front() <= i - k) {
            high.pop_front();
        }
        if (low.front() <= i - k) {
            low.pop_front();
        }
        if (i >= k - 1) {
            long long swing = (long long)value[high.front()] - value[low.front()];
            cout << swing << (i + 1 < n ? ' ' : '\n');
        }
    }
    return 0;
}
