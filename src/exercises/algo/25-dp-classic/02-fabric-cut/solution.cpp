#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, length;
    cin >> n >> length;
    vector<long long> best(length + 1, 0);
    for (int i = 0; i < n; i++) {
        int piece;
        long long price;
        cin >> piece >> price;
        for (int c = piece; c <= length; c++) {
            best[c] = max(best[c], best[c - piece] + price);
        }
    }
    cout << best[length] << '\n';
    return 0;
}
