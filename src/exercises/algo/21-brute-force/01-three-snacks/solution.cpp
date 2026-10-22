#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, budget;
    cin >> n >> budget;
    vector<int> price(n);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    int best = -1;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                int total = price[i] + price[j] + price[k];
                if (total <= budget && total > best) {
                    best = total;
                }
            }
        }
    }
    cout << best << '\n';
    return 0;
}
