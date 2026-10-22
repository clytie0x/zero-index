#include <bits/stdc++.h>
using namespace std;

#define MAX_PRICE 1000000
int before[MAX_PRICE + 1];

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
    long long ways = 0;
    for (int j = 0; j < n; j++) {
        for (int l = j + 1; l < n; l++) {
            int need = k - price[j] - price[l];
            if (need >= 1 && need <= MAX_PRICE) {
                ways += before[need];
            }
        }
        before[price[j]]++;
    }
    cout << ways << '\n';
    return 0;
}
