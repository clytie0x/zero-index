#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string cloth;
    cin >> cloth;
    int n = cloth.size();
    for (int p = 1; p <= n; p++) {
        bool repeats = true;
        for (int i = p; i < n; i++) {
            if (cloth[i] != cloth[i - p]) {
                repeats = false;
                break;
            }
        }
        if (repeats) {
            cout << p << '\n';
            return 0;
        }
    }
    return 0;
}
