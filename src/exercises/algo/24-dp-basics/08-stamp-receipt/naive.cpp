#include <bits/stdc++.h>
using namespace std;

vector<int> prices;
vector<int> chosen;
bool found = false;

void try_stamps(int left, int max_index, int stamps_left)
{
    if (found) {
        return;
    }
    if (left == 0 && stamps_left == 0) {
        found = true;
        return;
    }
    if (left == 0 || stamps_left == 0) {
        return;
    }
    for (int i = max_index; i < (int)prices.size(); i++) {
        if (prices[i] <= left) {
            chosen.push_back(prices[i]);
            try_stamps(left - prices[i], i, stamps_left - 1);
            if (found) {
                return;
            }
            chosen.pop_back();
        }
    }
}

int main()
{
    int n, target;
    cin >> n >> target;
    prices = vector<int>(n);
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }
    sort(prices.rbegin(), prices.rend());
    for (int k = 1; k <= target; k++) {
        try_stamps(target, 0, k);
        if (found) {
            cout << k << '\n';
            for (int i = 0; i < k; i++) {
                cout << chosen[i] << (i + 1 < k ? ' ' : '\n');
            }
            return 0;
        }
    }
    cout << -1 << '\n';
    return 0;
}
