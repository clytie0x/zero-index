#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long drop;
    cin >> n >> drop;
    vector<long long> price(n);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    long long count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (price[i] - price[j] > drop) {
                count++;
            }
        }
    }
    cout << count << '\n';
    return 0;
}
