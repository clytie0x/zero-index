#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k, q;
    cin >> k >> q;
    string pattern = "V";
    for (int round = 2; round <= k; round++) {
        string flipped = pattern;
        reverse(flipped.begin(), flipped.end());
        for (int i = 0; i < (int)flipped.size(); i++) {
            flipped[i] = flipped[i] == 'V' ? 'M' : 'V';
        }
        pattern = pattern + "V" + flipped;
    }
    for (int i = 0; i < q; i++) {
        long long p;
        cin >> p;
        cout << pattern[p - 1] << '\n';
    }
    return 0;
}
