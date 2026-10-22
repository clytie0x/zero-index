#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    cin >> n >> k;
    vector<int> price(n);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    nth_element(price.begin(), price.begin() + (k - 1), price.end());
    long long total = 0;
    for (int i = 0; i < k; i++) {
        total += price[i];
    }
    cout << total << '\n';
    return 0;
}
