#include <bits/stdc++.h>
using namespace std;

char crease(int k, long long p)
{
    long long middle = 1LL << (k - 1);
    if (p == middle) {
        return 'V';
    }
    if (p < middle) {
        return crease(k - 1, p);
    }
    char mirrored = crease(k - 1, (1LL << k) - p);
    return mirrored == 'V' ? 'M' : 'V';
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k, q;
    cin >> k >> q;
    for (int i = 0; i < q; i++) {
        long long p;
        cin >> p;
        cout << crease(k, p) << '\n';
    }
    return 0;
}
