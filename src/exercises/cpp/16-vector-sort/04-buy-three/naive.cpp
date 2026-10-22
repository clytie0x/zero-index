#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> price(n);
    for (int &p : price) {
        cin >> p;
    }
    for (int i = 0; i < n - 1; i++) {
        int max_index = i;
        for (int j = i + 1; j < n; j++) {
            if (price[j] > price[max_index]) {
                max_index = j;
            }
        }
        swap(price[i], price[max_index]);
    }
    long long total = 0;
    for (int i = 0; i < n; i++) {
        if (i % 3 != 2) {
            total += price[i];
        }
    }
    cout << total << '\n';
    return 0;
}
