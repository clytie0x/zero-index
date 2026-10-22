#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, length;
    cin >> n >> length;
    vector<long long> best(length + 1, 0);
    for (int i = 0; i < n; i++) {
        int piece;
        long long price;
        cin >> piece >> price;
        vector<long long> next = best;
        for (int c = 0; c <= length; c++) {
            for (int count = 1; (long long)count * piece <= c; count++) {
                next[c] = max(next[c], best[c - count * piece] + count * price);
            }
        }
        best = next;
    }
    cout << best[length] << '\n';
    return 0;
}
