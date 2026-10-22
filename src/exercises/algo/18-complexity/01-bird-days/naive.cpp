#include <bits/stdc++.h>
using namespace std;

bool seen[1000001];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> bird(n);
    for (int i = 0; i < n; i++) {
        cin >> bird[i];
    }
    for (int t = 0; t < q; t++) {
        int k;
        cin >> k;
        int kinds = 0;
        for (int i = 0; i < k; i++) {
            if (!seen[bird[i]]) {
                seen[bird[i]] = true;
                kinds++;
            }
        }
        for (int i = 0; i < k; i++) {
            seen[bird[i]] = false;
        }
        cout << kinds << '\n';
    }
    return 0;
}
