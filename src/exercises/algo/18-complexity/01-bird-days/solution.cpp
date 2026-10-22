#include <bits/stdc++.h>
using namespace std;

bool seen[1000001];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> kinds(n + 1);
    kinds[0] = 0;
    for (int i = 1; i <= n; i++) {
        int b;
        cin >> b;
        kinds[i] = kinds[i - 1];
        if (!seen[b]) {
            seen[b] = true;
            kinds[i]++;
        }
    }
    for (int t = 0; t < q; t++) {
        int k;
        cin >> k;
        cout << kinds[k] << '\n';
    }
    return 0;
}
