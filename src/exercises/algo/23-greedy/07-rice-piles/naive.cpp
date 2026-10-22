#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> piles(n);
    for (int i = 0; i < n; i++) {
        cin >> piles[i];
    }
    long long cost = 0;
    while (piles.size() > 1) {
        int a = 0;
        for (int i = 1; i < (int)piles.size(); i++) {
            if (piles[i] < piles[a]) {
                a = i;
            }
        }
        long long first = piles[a];
        piles[a] = piles.back();
        piles.pop_back();
        int b = 0;
        for (int i = 1; i < (int)piles.size(); i++) {
            if (piles[i] < piles[b]) {
                b = i;
            }
        }
        piles[b] += first;
        cost += piles[b];
    }
    cout << cost << '\n';
    return 0;
}
